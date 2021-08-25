from core.input import InputChannel
from core.factory import GameObjectFactory
from core.scene import Scene
from core.engine import Engine

class Game:
    def __init__(self, scene: Scene, engine: Engine, channel: InputChannel) -> None:
        self.scene = scene
        self.engine = engine
        self.channel = channel
        self.factory = GameObjectFactory(scene, channel, engine)

    def start(self):
        raise NotImplementedError()

    def pause(self):
        raise NotImplementedError()

    def resume(self):
        raise NotImplementedError()

    def save(self):
        raise NotImplementedError()

    def exit(self):
        raise NotImplementedError()
    