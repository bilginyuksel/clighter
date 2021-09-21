from .input import InputChannel
from .factory import GameObjectFactory
from .scene import Scene
from .engine import Engine


class Game:
    def __init__(self, scene: Scene, engine: Engine, channel: InputChannel) -> None:
        self.scene = scene
        self.engine = engine
        self.channel = channel

        # Create the game object factory for the first time.
        factory = GameObjectFactory()
        factory.scene = scene
        factory.channel = channel
        factory.engine = engine

    def start(self):
        """
        Start the engine, channel and scene. 
        """
        raise NotImplementedError()

    def exit(self):
        """
        Exit the game. 
        """
        raise NotImplementedError()
