from scene import Scene, Dimension, GameObject, Position
from engine import Engine

class CLIScene(Scene):
    def draw(self):
        print(self.objects)

cli = CLIScene(Dimension(400, 500))
engine = Engine(cli)
character = GameObject(cli, Position(10, 10), Dimension(30, 10))
cli.draw()
# engine.start()
engine.stop()