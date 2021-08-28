from core.scene import GameObject, Position
from core.factory import GameObjectFactory
from cli.game import CLIGame


class Character(GameObject):
    def __init__(self, position: Position) -> None:
        super().__init__(position, None, filepath='assets/character.txt',
                         obstacle=False, controllable=True)

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
            bullet = Bullet(Position(self.position.x+2, self.position.y+5))
            GameObjectFactory().use(bullet, scene=True)


class Bullet(GameObject):
    def __init__(self, position: Position) -> None:
        super().__init__(position, dimension=None, filepath='assets/bullet.txt',
                         obstacle=False, controllable=False)
        self.velocity = 0

    def update(self):
        self.velocity += 0.5
        if self.velocity >= 1:
            self.position.y += 1
            self.velocity = 0


class Monster(GameObject):
    def __init__(self, position: Position) -> None:
        super().__init__(position, dimension=None, filepath='assets/monster.txt',
                         obstacle=False, controllable=False)

    def collide(self, game_object):
        if isinstance(game_object, Bullet):
            self.destroy()
            game_object.destroy()


def main():
    g = CLIGame()
    factory = GameObjectFactory()
    character = Character(Position(10, 10))
    monster = Monster(Position(30, 50))
    factory.use(character, channel=True, scene=True)
    factory.use(monster, scene=True)
    g.start()


if __name__ == '__main__':
    main()
