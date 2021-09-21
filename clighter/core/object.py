from .util.files import read_from_file
from .animation import AnimationMixin
from .common import generate_id
from .dimension import Dimension
from .position import Position
from .rect import Rectangle


class GameObject:
    def __init__(self, position: Position, dimension: Dimension, filepath=None, obstacle=False, controllable=False, z_index=0, trigger_collision=True) -> None:
        """
        Construct a game object.
        `position`: Initialize the position of the game object.
        `dimension`: Area of the game object.
        `filepath`: Give a .txt file to automatically draw object. If you give this parameter
            then dimension will be computed automatically.
        `obstacle`: If the object is obstacle that means it is solid.
        `controllable`: If this field is true that means the object can be controlled but if it is false
            that means object can't be controlled by inputs.
        `z_index`: z axis index of an object. z-index used to identify which objects are in the same layer.
            Assign different z-index for background objects and the real objects.
            Objects has the same z-index can be collided with each other. If you don't want the collision
            effect you can change their z-indexes. Also if z-index is smaller than zero the engine will
            automatically skip that objects collision effect. If you have background drawing you should
            give z-index smaller than zero. 
            Also it represents the drawing order. Greater z-index will be drawn last.
        `trigger_collision`: If it is true the engine will compute the object for collisions.
            This field is very important for optimization. If you want to compute collision for 2
            different objects then it is enough to have this field True for one of them. Both of them
            will be unnecessary and hard to compute.
            For instance: If you want to handle the collision effect between the bullets and the monster.
            It will be hard to compute collision effect for every bullet. So you should change bullets
            `trigger_collision` to false but you should open monster's `trigger_colliision` to true.
            You can easily catch the collision effect from the monster.
        """
        self._id = generate_id()
        self.controllable = controllable
        # If you will not use `collide` function for the game object
        # you should set `trigger_collision` to False to optimize the engine.
        self.trigger_collision = trigger_collision
        self.obstacle = obstacle
        self.position = position
        self.dimension = dimension
        self.z_index = z_index
        self.drawing = None

        if filepath is not None:
            self.drawing, self.dimension = read_from_file(filepath)

        self._delay_frames_to_destroy = None

    def _update(self):
        # Internal update method, to handle general game object concerns
        if self._delay_frames_to_destroy is not None:
            self._delay_frames_to_destroy -= 1
            if self._delay_frames_to_destroy <= 0:
                self.destroy()
        self.update()
        if isinstance(self, AnimationMixin):
            self.anim_update()

    def update(self):
        """
        Game objects update function will be ran `FPS` times in a second.
        Use this function to apply changes to the object on every frame.
        """
        pass

    def collide(self, game_object):
        """
        Game objects can collide with each other if they have the same z_index and
        if they are collidable. 
        Whenever a game object collides this function will be triggered by engine.
        Collide function will give you the collided `game_object` as a parameter.
        """
        pass

    def destroy(self, delay_frames: int = None, z_index=float('-inf')):
        """
        Call this function to destroy the game object. 
        You can call this function without `delay_frames` parameter and it will destroy
        the object immediately. If you give `delay_frames` parameter then the object 
        will be destroy after the `delay_frames` times frames executed.
        """
        if delay_frames is not None:
            self._delay_frames_to_destroy = delay_frames
            self.z_index = z_index
        else:
            self._scene.remove(self)
            if self.controllable:
                self._channel.remove(self)

    def on_key_pressed(self, key: chr):
        """
        If object is not a `controllable` object and not subscribed to input channel 
        this function will be useless.

        If object is subscribed to the input channel and is controllable then
        whenever a keystroke captured by the system this `on_key_pressed` function will be
        triggered and `key` parameter will be passed to the object.
        """
        raise NotImplementedError()

    def attach(self, scene):
        """
        Attach the game object to scene.
        After the object attached it will be rendered in the screen on every frame.
        """
        self._scene = scene
        scene.add(self)

    def subscribe(self, channel):
        """
        Subscribe game object to input channel.
        After the object subscribed to the input channel `on_key_pressed` function will be called
        whenever key stroke is captured by the system.
        """
        self._channel = channel
        channel.subscribe(self)

    def rect(self) -> Rectangle:
        """
        Return the current rectangle of the object.
        You can refer this rectangle as the object's collision skeleton.
        """
        return Rectangle(self.position, self.dimension)

    def get_id(self):
        """
        Every object has a unique id. 
        This function will return the object's id.
        """
        return self._id
