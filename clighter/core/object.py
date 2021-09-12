from .util.files import read_from_file
from .animation import AnimationMixin
from .common import generate_id
from .dimension import Dimension
from .position import Position
from .rect import Rectangle


class GameObject:
    def __init__(self, position: Position, dimension: Dimension, filepath=None, obstacle=False, controllable=False, z_index=0, trigger_collision= True) -> None:
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
        pass

    def collide(self, game_object):
        pass

    def destroy(self, delay_frames: int = None, z_index= float('-inf')):
        if delay_frames is not None:
            self._delay_frames_to_destroy = delay_frames
            self.z_index = z_index
        else:
            self._scene.remove(self)
            if self.controllable:
                self._channel.remove(self)

    def on_key_pressed(self, key: chr):
        raise NotImplementedError()

    def attach(self, scene):
        self._scene = scene
        scene.add(self)

    def subscribe(self, channel):
        self._channel = channel
        channel.subscribe(self)

    def rect(self) -> Rectangle:
        return Rectangle(self.position, self.dimension)

    def get_id(self):
        return self._id
