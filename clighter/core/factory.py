from .util import Singleton
from .position import Position
from .dimension import Dimension
from .object import GameObject


class GameObjectFactory(metaclass=Singleton):
    def __init__(self):
        """
        Constructor of the game object factory.
        Once this object created when you try to create a new factory
        you will have the old one because it is singleton.
        You can use this class to manage game object in the game ecosystem.
        """
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
        """
        Create a basic game object.  
        """
        game_object = GameObject(
            position, dimension, obstacle=obstacle, controllable=controllable, filepath=filepath)
        self.put(game_object, channel, scene)
        return game_object

    def put(self, game_object: GameObject, channel=False, scene=False):
        """
        Put method can be used to:
            - subscribe game object to channel
            - attach game object to scene 
        """
        if scene:
            game_object.attach(self.scene)

        if channel:
            game_object.subscribe(self.channel)
