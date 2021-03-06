import sys
# It is very important to put sys.path.append line of code before
# importing the clighter library.
# Because to let this file use clighter, it needs to check the module
# at 2 depth upper. 
sys.path.append('../..')

import time
import random


from clighter import *


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
            bullet = Bullet(Position(self.position.x+13,
                                     self.position.y+3), 'right')
            GameObjectFactory().put(bullet, scene=True)
        elif key == 'n':
            bullet = Bullet(Position(self.position.x, self.position.y), 'left')
            GameObjectFactory().put(bullet, scene=True)


class Bullet(GameObject):
    def __init__(self, position: Position, direction: str) -> None:
        super().__init__(position, dimension=None, filepath='assets/bullet.txt',
                         obstacle=False, controllable=False, trigger_collision=False)
        self.direction = direction

    def update(self):
        if self.direction == 'left':
            self.position.x -= 1
        elif self.direction == 'right':
            self.position.x += 1


class Monster(GameObject, AnimationMixin):
    def __init__(self, position: Position) -> None:
        GameObject.__init__(self, position, dimension=None, filepath='assets/monster.txt',
                            obstacle=False, controllable=False)
        AnimationMixin.__init__(self)

        self.add_animation('destroy', AnimationFrame(
            'assets/explosion_1.txt', 10))
        self.add_animation('destroy', AnimationFrame(
            'assets/explosion_2.txt', 10))

    def collide(self, game_object):
        if isinstance(game_object, Bullet):
            self.animate('destroy')
            self.destroy(delay_frames=20)
            game_object.destroy()


def main():
    g = CLIGame()
    factory = GameObjectFactory()
    character = Character(Position(10, 10))
    factory.put(character, channel=True, scene=True)
    g.start()
    count = 10
    while count > 0:
        rand_x, rand_y = random.randint(50, 150), random.randint(5, 40)
        monster = Monster(Position(rand_x, rand_y))
        factory.put(monster, scene=True)
        count -= 1
        time.sleep(1)


if __name__ == '__main__':
    main()
