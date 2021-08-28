from core.input import InputChannel
from core.factory import GameObjectFactory
from core.scene import Scene
from core.engine import Engine


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
        raise NotImplementedError()

    def exit(self):
        raise NotImplementedError()
