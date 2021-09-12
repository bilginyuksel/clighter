from .dimension import Dimension
from .object import GameObject


class Scene:
    def __init__(self, dimension: Dimension):
        self.dimension = dimension
        self.objects: dict[str, GameObject] = {}

    def add(self, obj: GameObject) -> None:
        self.objects[obj.get_id()] = obj

    def remove(self, obj: GameObject) -> None:
        if obj.get_id() in self.objects:
            del self.objects[obj.get_id()]

    def draw(self):
        raise NotImplementedError()
