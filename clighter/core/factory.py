from .util import Singleton
from .position import Position
from .dimension import Dimension
from .object import GameObject


class GameObjectFactory(metaclass=Singleton):
    def __init__(self):
        self.scene = None
        self.channel = None
        self.engine = None

    def create(self, position: Position,
               dimension: Dimension,
               obstacle=False,
               controllable=False,
               channel=False,
               scene=False,
               filepath=None) -> GameObject:
        game_object = GameObject(
            position, dimension, obstacle=obstacle, controllable=controllable, filepath=filepath)
        self.put(game_object, channel, scene)
        return game_object

    def put(self, game_object: GameObject, channel=False, scene=False):
        if scene:
            game_object.attach(self.scene)

        if channel:
            game_object.subscribe(self.channel)
