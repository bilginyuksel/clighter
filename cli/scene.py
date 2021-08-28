from cli.util.windows import clear_cli, fast_print
from core.dimension import Dimension
from core.object import GameObject
from core.scene import Scene


class CLIScene(Scene):
    def __init__(self, dimension: Dimension):
        super().__init__(dimension)

        self.rows, self.columns = dimension.height, dimension.width
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
            w, h = v.dimension.width, v.dimension.height
            if not v.controllable and (x >= self.columns or y >= self.rows or x+w < 0 or y+h < 0):
                items_to_delete.append(k)
                continue
            self._draw_object(v)

        for to_delete in items_to_delete:
            del self.objects[to_delete]

    def _draw_object(self, obj: GameObject):
        drawing = obj.drawing
        for i in range(len(drawing)):
            for j in range(len(drawing[i])):
                is_greater = j+obj.position.x >= self.columns or i+obj.position.y >= self.rows
                is_lower = obj.position.x+j < 0 or obj.position.y+i < 0
                if is_greater or is_lower:
                    continue
                self.map[i+obj.position.y][j+obj.position.x] = drawing[i][j]

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
