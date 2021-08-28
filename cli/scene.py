from cli.util.windows import clear_cli, fast_print
from core.scene import Dimension, GameObject, Scene


class CLIScene(Scene):
    def __init__(self, dimension: Dimension):
        super().__init__(dimension)

        self.rows, self.columns = dimension.width, dimension.height
        self.map = [[' ' for _ in range(self.columns)]
                    for _ in range(self.rows)]

    def draw(self):
        clear_cli()
        fast_print(self._draw())

    def _clean(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.map[i][j] = ' '

    def _draw_objects(self):
        items_to_delete = []
        for k, v in self.objects.items():
            x, y = v.position.x, v.position.y
            # w, h = v.dimension.width, v.dimension.height
            if not v.controllable and (x >= self.rows or y >= self.columns or x < 0 or y < 0):
                items_to_delete.append(k)
                continue
            self._draw_object(v)

        for to_delete in items_to_delete:
            del self.objects[to_delete]

    def _draw_object(self, obj: GameObject):
        drawing = obj.drawing
        for i in range(len(drawing)):
            for j in range(len(drawing[i])):
                is_greater = i+obj.position.x >= self.rows or j+obj.position.y >= self.columns
                is_lower = obj.position.x < 0 or obj.position.y < 0
                if is_greater or is_lower:
                    continue
                self.map[i+obj.position.x][j+obj.position.y] = drawing[i][j]

    def _draw(self):
        self._clean()
        self._draw_objects()
        row = []
        for i in range(self.rows):
            column = []
            for j in range(self.columns):
                column.append(self.map[i][j])
            row.append(''.join(column))
        return '\n'.join(row)
