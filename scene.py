from common import generate_id


class Dimension:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

class VisibleRegion:
    def __init__(self, center: Position, dimension: Dimension) -> None:
        self.center = center
        self.dimension = dimension

class DrawableObject:
    def __init__(self, position: Position, dimension: Dimension) -> None:
        self._id = generate_id()
        self.position = position
        self.dimension = dimension
    
    def get_id(self):
        return self._id

class Scene:
    def __init__(self, dimension: Dimension):
        self.dimension = dimension
        self.drawable_objects = {}
    
    def add(self, obj: DrawableObject) -> None:
        self.drawable_objects[obj.get_id()] = obj

    def remove(self, obj: DrawableObject) -> None:
        self.drawable_objects.pop(obj.get_id())

    def draw(self):
        raise NotImplementedError()
