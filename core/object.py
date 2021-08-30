from core.animation import AnimationMixin
from core.common import generate_id
from core.dimension import Dimension
from core.position import Position
from core.rect import Rectangle


class GameObject:
    def __init__(self, position: Position, dimension: Dimension, filepath=None, obstacle=False, controllable=False) -> None:
        self._id = generate_id()
        self.controllable = controllable
        self.obstacle = obstacle
        self.position = position
        self.dimension = dimension
        self.drawing = None

        if filepath is not None:
            with open(filepath, 'r') as f:
                lines = f.read().split('\n')
                axis_y, axis_x = len(lines), max(
                    [len(line) for line in lines])
                self.dimension = Dimension(axis_y, axis_x)
                self.drawing = [
                    [' ' for _ in range(axis_x)] for _ in range(axis_y)]
                for i in range(len(lines)):
                    for j in range(len(lines[i])):
                        self.drawing[i][j] = lines[i][j]

    def _update(self):
        # Internal update method, to handle general game object concerns
        self.update()
        if isinstance(self, AnimationMixin):
            self.anim_update()

    def update(self):
        pass

    def collide(self, game_object):
        pass

    def destroy(self):
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
