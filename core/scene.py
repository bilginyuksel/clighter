from core.common import generate_id

class Dimension:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

class GameObject:
    def __init__(self, position: Position, dimension: Dimension, obstacle= False, controllable=False) -> None:
        self._id = generate_id()
        self.controllable = controllable
        self.obstacle = obstacle
        self.position = position
        self.dimension = dimension
    
    def update(self):
        pass

    def collide(self, game_object):
        pass

    def destroy(self):
        self._scene.remove(self._id)

    def on_key_pressed(self, key: chr):
        pass

    def attach(self, scene):
        scene.add(self)
    
    def subscribe(self, channel):
        channel.subscribe(self)

    def get_id(self):
        return self._id

class Scene:
    def __init__(self, dimension: Dimension):
        self.dimension = dimension
        self.objects = {}
    
    def add(self, obj: GameObject) -> None:
        self.objects[obj.get_id()] = obj

    def remove(self, obj: GameObject) -> None:
        self.objects.pop(obj.get_id())

    def draw(self):
        raise NotImplementedError()
