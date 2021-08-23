from core.scene import Scene
from core.engine import Engine

class Game:
    def __init__(self, scene: Scene, engine: Engine) -> None:
        self.scene = scene
        self.engine = engine

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
    