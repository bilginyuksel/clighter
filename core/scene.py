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
    def __init__(self, position: Position, dimension: Dimension, filepath=None, obstacle=False, controllable=False) -> None:
        self._id = generate_id()
        self.controllable = controllable
        self.obstacle = obstacle
        self.position = position
        self.dimension = dimension
        self.drawing = None

        if filepath is not None:
            with open(filepath, 'r') as f:
                lines = f.read().split('\n')
                max_row, max_col = len(lines), max(
                    [len(line) for line in lines])
                self.dimension = Dimension(max_row, max_col)
                self.drawing = [
                    [' ' for _ in range(max_col)] for _ in range(max_row)]
                for i in range(len(lines)):
                    for j in range(len(lines[i])):
                        self.drawing[i][j] = lines[i][j]

    def update(self):
        pass

    def collide(self, game_object):
        pass

    def destroy(self):
        self._scene.remove(self)

    def on_key_pressed(self, key: chr):
        raise NotImplementedError()

    def attach(self, scene):
        self._scene = scene
        scene.add(self)

    def subscribe(self, channel):
        channel.subscribe(self)

    def get_id(self):
        return self._id


class Scene:
    def __init__(self, dimension: Dimension):
        self.dimension = dimension
        self.objects: dict[str, GameObject] = {}

    def add(self, obj: GameObject) -> None:
        self.objects[obj.get_id()] = obj

    def remove(self, obj: GameObject) -> None:
        self.objects.pop(obj.get_id())

    def draw(self):
        raise NotImplementedError()
