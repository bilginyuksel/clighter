from ..core import Dimension, Game, Engine

from .scene import CLIScene
from .input import CLIInputChannel


class CLIGame(Game):
    def __init__(self) -> None:
        self.scene = CLIScene(Dimension(50, 180))
        self.engine = Engine(self.scene, fps=60)
        self.channel = CLIInputChannel(self._create_channel_callbacks())

        super().__init__(self.scene, self.engine, self.channel)

    def start(self):
        self.engine.start()
        self.channel.start()

    def exit(self):
        self.engine.stop()
        self.channel.stop()

    def _create_channel_callbacks(self):
        return {
            'q': self.exit
        }
