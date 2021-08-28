from core.scene import GameObject, Position, Dimension
from core.factory import GameObjectFactory
from cli.game import CLIGame


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


g = CLIGame()
character = Character(Position(10, 10), Dimension(100, 200))
g.factory.extend_game_object(character, channel=True, scene=True)
character.factory = g.factory
g.start()
