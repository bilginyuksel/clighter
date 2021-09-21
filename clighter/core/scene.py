from .dimension import Dimension
from .object import GameObject


class Scene:
    def __init__(self, dimension: Dimension):
        self.dimension = dimension
        self.objects: dict[str, GameObject] = {}

    def add(self, obj: GameObject) -> None:
        """
        Add object to scene. When you add a new object to scene
        after that object will be drawn to scene in every `draw` 
        function call. 
        """
        self.objects[obj.get_id()] = obj

    def remove(self, obj: GameObject) -> None:
        """
        Remove an object from the scene if it exists. 
        """
        if obj.get_id() in self.objects:
            del self.objects[obj.get_id()]

    def draw(self):
        """
        Draws all objects in the scene to the screen
        This function will be ran `FPS` times in a second.
        """
        raise NotImplementedError()
    
    def clear(self):
        """
        Removes all objects from the scene. It could be used at the end of the game
        or changing the levels and maps. 
        """
        self.objects.clear()
