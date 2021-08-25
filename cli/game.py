from core.scene import Dimension, GameObject, Position
from core.game import Game

from cli.scene import CLIScene
from cli.input import CLIInputChannel
from cli.engine import CLIEngine


class CLIGame(Game):
    def __init__(self) -> None:
        self.scene = CLIScene(Dimension(500, 400))
        self.engine = CLIEngine(self.scene)
        self.channel = CLIInputChannel(self._create_channel_callbacks())
        
        super().__init__(self.scene, self.engine, self.channel)

    def start(self):
        self.engine.start()
        self.channel.start()
        self._prepare()
    
    def pause(self):
        return super().pause()
    
    def resume(self):
        return super().resume()

    def save(self):
        return super().save()

    def exit(self):
        self.engine.stop()
    
    def _prepare(self):
        # Create new character class
        character = self.factory.create_game_object(Position(10, 50), Dimension(100, 200), controllable=True, channel=True, scene=True)
        print(character.get_id())
    
    def _create_channel_callbacks(self):
        return {
            'q': self.exit,
            's': self.save,
            'r': self.resume,
            'p': self.pause
        }