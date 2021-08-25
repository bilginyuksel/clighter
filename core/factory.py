from core.scene import Dimension, Position, Scene, GameObject


class GameObjectFactory:
    def __init__(self, scene: Scene, channel, engine):
        self.scene = scene
        self.channel = channel
        self.engine = engine

    def create_game_object(self, position: Position, dimension: Dimension, obstacle=False, controllable=False, channel=False, scene=False) -> GameObject:
        game_object = GameObject(
            position, dimension, obstacle=obstacle, controllable=controllable)
        self.extend_game_object(game_object, channel, scene)
        return game_object

    def extend_game_object(self, game_object: GameObject, channel=False, scene=False):
        if scene:
            game_object.attach(self.scene)
            print('Attached to scene')
        if channel:
            game_object.subscribe(self.channel)
            print('Subscribed to channel')
