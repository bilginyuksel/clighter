from core.object import GameObject
from core.position import Position
from core.factory import GameObjectFactory
from cli.game import CLIGame


class Character(GameObject):
    def __init__(self, position: Position) -> None:
        super().__init__(position, None, filepath='assets/character.txt',
                         obstacle=False, controllable=True)

    def on_key_pressed(self, key: chr):
        if key == 's':
            self.position.y += 3
        elif key == 'w':
            self.position.y -= 3
        elif key == 'd':
            self.position.x += 3
        elif key == 'a':
            self.position.x -= 3
        elif key == 'm':
            bullet = Bullet(Position(self.position.x+13, self.position.y+3))
            GameObjectFactory().use(bullet, scene=True)


class Bullet(GameObject):
    def __init__(self, position: Position) -> None:
        super().__init__(position, dimension=None, filepath='assets/bullet.txt',
                         obstacle=False, controllable=False)

    def update(self):
        self.position.x += 1


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
    monster = Monster(Position(80, 30))
    factory.use(character, channel=True, scene=True)
    factory.use(monster, scene=True)
    g.start()


if __name__ == '__main__':
    main()
