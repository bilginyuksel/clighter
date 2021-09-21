import sys
sys.path.append('../..')

import clighter

class Character(clighter.GameObject):
    def __init__(self):
        super().__init__(clighter.Position(10, 10), None, filepath='assets/mario.txt', obstacle=False, controllable=True)

if __name__ == '__main__':
    game = clighter.CLIGame()
    factory = clighter.GameObjectFactory()
    c = Character()
    factory.put(c, channel=True, scene=True)
    game.start()
