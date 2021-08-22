from common import generate_id

class Dimension:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

class GameObject:
    def __init__(self, scene, position: Position, dimension: Dimension, obstacle= False) -> None:
        self._id = generate_id()
        self._scene = scene
        self.obstacle = obstacle
        self.position = position
        self.dimension = dimension

        self._scene.add(self)
    
    def update(self):
        pass

    def collide(self, game_object):
        pass

    def get_id(self):
        return self._id

    def _update(self):
        pass
    
    def _destroy(self):
        self._scene.remove(self._id)
    
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
