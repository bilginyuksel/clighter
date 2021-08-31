from core.util.files import read_from_file
from core.animation import AnimationMixin
from core.common import generate_id
from core.dimension import Dimension
from core.position import Position
from core.rect import Rectangle

UP = 0
LEFT = 1
RIGHT = 2
DOWN = 3
STANDING = -1


class GameObject:
    def __init__(self, position: Position, dimension: Dimension, filepath=None, obstacle=False, controllable=False, z_index=0) -> None:
        self._id = generate_id()
        self.controllable = controllable
        self.obstacle = obstacle
        self.position = position
        self.dimension = dimension
        self.z_index = z_index
        self.state = STANDING
        self.drawing = None

        if filepath is not None:
            self.drawing, self.dimension = read_from_file(filepath)

        self._delay_frames_to_destroy = None

        self.incr_x = None
        self.incr_y = None
        self.decr_x = None
        self.decr_y = None

    def _update(self):
        if self.incr_x and self.incr_x > 0:
            self.incr_x -= 1
            self.position.x += 1
        if self.incr_y and self.incr_y > 0:
            self.incr_y -= 1
            self.position.y += 1
        if self.decr_x and self.decr_x > 0:
            self.decr_x -= 1
            self.position.x -= 1
        if self.decr_y and self.decr_y > 0:
            self.decr_y -= 1
            self.position.y -= 1

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

    def update_pos(self, x=None, y=None):
        if x and x > 0:
            self.incr_x = x
        if y and y > 0:
            self.incr_y = y
        if x and x < 0:
            self.decr_x = abs(x)
        if y and y < 0:
            self.decr_y = abs(y)

    def destroy(self, delay_frames: int = None, z_index=float('-inf')):
        if delay_frames is not None:
            self._delay_frames_to_destroy = delay_frames
            self.z_index = z_index
        else:
            self._scene.remove(self)

    def on_key_pressed(self, key: chr):
        raise NotImplementedError()

    def attach(self, scene):
        self._scene = scene
        scene.add(self)

    def subscribe(self, channel):
        channel.subscribe(self)

    def rect(self) -> Rectangle:
        return Rectangle(self.position, self.dimension)

    def get_id(self):
        return self._id
