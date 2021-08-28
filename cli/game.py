from core.factory import GameObjectFactory
from core.scene import Dimension, GameObject, Position
from core.game import Game

from cli.scene import CLIScene
from cli.input import CLIInputChannel
from cli.engine import CLIEngine


class CLIGame(Game):
    def __init__(self) -> None:
        self.scene = CLIScene(Dimension(70, 50))
        self.engine = CLIEngine(self.scene, fps=60)
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
        character = Character(Position(10, 10), Dimension(100, 200))
        self.factory.extend_game_object(character, channel=True, scene=True)
        character.factory = self.factory

    def _create_channel_callbacks(self):
        return {
            'q': self.exit,
            # 's': self.save,
            'r': self.resume,
            'p': self.pause
        }


class Character(GameObject):
    def __init__(self, position: Position, dimension: Dimension) -> None:
        super().__init__(position, dimension, filepath='assets/character.txt',
                         obstacle=False, controllable=True)
        self.factory: GameObjectFactory = None

    def on_key_pressed(self, key: chr):
        if key == 's':
            self.position.x += 3
        elif key == 'w':
            self.position.x -= 3
        elif key == 'd':
            self.position.y += 3
        elif key == 'a':
            self.position.y -= 3
        elif key == 'm':
            bullet = Bullet(Position(self.position.x+2, self.position.y+5),
                            Dimension(100, 200))
            self.factory.extend_game_object(bullet, scene=True)


class Bullet(GameObject):
    def __init__(self, position: Position, dimension=None) -> None:
        super().__init__(position, dimension=None, filepath='assets/bullet.txt',
                         obstacle=False, controllable=False)
        self.velocity = 0

    def update(self):
        self.velocity += 0.5
        if self.velocity >= 1:
            self.position.y += 1
            self.velocity = 0
