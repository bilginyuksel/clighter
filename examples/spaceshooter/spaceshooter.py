import sys
# It is very important to put sys.path.append line of code before
# importing the clighter library.
# Because to let this file use clighter, it needs to check the module
# at 2 depth upper. 
sys.path.append('../..')

import time
import random
from clighter import (
    CLIGame, GameObject, GameObjectFactory, Position,
    Dimension, AnimationFrame, AnimationMixin
)


global game_score
game_score = 0


class Bullet(GameObject):
    def __init__(self, position, direction, group):
        filepath = 'assets/%s_bullet.txt' % direction
        GameObject.__init__(self, position, dimension=None, filepath=filepath,
                            obstacle=False, controllable=False, trigger_collision=False)
        self.direction = direction
        self.group = group

    def update(self):
        if self.direction == 'left':
            self.position.x -= 1
        elif self.direction == 'right':
            self.position.x += 1


class SpaceShip(GameObject):
    def __init__(self):
        GameObject.__init__(self, position=Position(10, 10), dimension=None, filepath='assets/spaceship.txt',
                            obstacle=False, controllable=True)
        self.group = 'ally'
        self.game = None
        self.game_over = None

    def collide(self, game_object):
        if isinstance(game_object, Bullet) and game_object.group != self.group:
            GameObjectFactory().put(self.game_over, scene=True)
            game_object.destroy()
            self.destroy()

    def on_key_pressed(self, key):
        if key == 's':
            self.position.y += 3
        elif key == 'w':
            self.position.y -= 3
        elif key == 'd':
            self.position.x += 3
        elif key == 'a':
            self.position.x -= 3
        elif key == 'm':
            bullet = Bullet(Position(self.position.x+5,
                            self.position.y+2), 'right', self.group)
            GameObjectFactory().put(bullet, scene=True)

#    def destroy(self, delayed_frames= None, z_index=float('-inf')):
#        super().destroy(delayed_frames= delayed_frames, z_index= z_index)
#
#        # do what you want game over
#        pass


class EnemyShip(GameObject, AnimationMixin):
    def __init__(self, position):
        GameObject.__init__(self, position=position, dimension=None, filepath='assets/enemy_ship.txt',
                            obstacle=False, controllable=False)
        AnimationMixin.__init__(self)

        self.group = 'enemy'
        self.fire_time = 100
        self.speed = 3

        self.add_animation('destroy', AnimationFrame(
            'assets/explosion_1.txt', 10))
        self.add_animation('destroy', AnimationFrame(
            'assets/explosion_2.txt', 10))

    def update(self):
        self.fire_time -= 1
        if self.fire_time <= 0:
            self.fire_time = 100
            self.fire()

        self.speed -= 1
        if self.speed <= 0:
            self.position.x -= 1
            self.speed = 3

    def fire(self):
        bullet = Bullet(Position(self.position.x-3,
                        self.position.y+1), 'left', self.group)
        GameObjectFactory().put(bullet, scene=True)

    def collide(self, game_object):
        if isinstance(game_object, Bullet) and game_object.group != self.group:
            global game_score
            game_score += 250
            self.animate('destroy')
            game_object.destroy()
            self.destroy(delay_frames=20)


class ScoreBoard(GameObject):
    def __init__(self):
        GameObject.__init__(self, Position(0, 0), dimension=Dimension(1, 16), filepath=None,
                            obstacle=False, controllable=False, z_index=float('inf'))

    def update(self):
        self.update_drawing()

    def update_drawing(self) -> str:
        global game_score
        scoreboard = 'Score: %d' % game_score
        self.drawing = [list(scoreboard)]


class GameOver(GameObject):
    def __init__(self):
        GameObject.__init__(self, Position(60, 16), dimension=Dimension(2, 20), filepath=None,
                            obstacle=False, controllable=False, z_index=float('-inf'))

        global game_score
        self.drawing = [list('Game Over'), list('Score: %d' % game_score)]

    def update(self):
        global game_score
        self.drawing = [list('Game Over'), list('Score: %d' % game_score)]


# main function of the script file
def main():
    game = CLIGame()
    scoreboard = ScoreBoard()
    ship = SpaceShip()
    ship.game = game
    ship.game_over = GameOver()

    # factory implementations
    factory = GameObjectFactory()
    factory.put(scoreboard, scene=True)
    factory.put(ship, scene=True, channel=True)

    game.start()

    count = 50
    while count > 0:
        count -= 10
        sub_count = 10
        while sub_count > 0:
            # axis_y = 50, axis_x = 180
            x_pos, y_pos = 176, random.randint(5, 45)
            enemy_ship = EnemyShip(Position(x_pos, y_pos))
            factory.put(enemy_ship, scene=True)
            time.sleep(0.3)
            sub_count -= 1
        time.sleep(1)


if __name__ == '__main__':
    main()
