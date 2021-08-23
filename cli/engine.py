from core.scene import Scene
from threading import Thread
from core.engine import Engine

class CLIEngine(Thread, Engine):
    def __init__(self, scene: Scene) -> None:
        Thread.__init__(self, group=None, target=self.start, name='cli_engine', args=self, kwargs=None, daemon=None)
        Engine.__init__(self, scene)
    
    def start(self) -> None:
        return super().start() 

    def run(self) -> None:
        self._start()