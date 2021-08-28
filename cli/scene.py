from cli.util.windows import clear_cli, fast_print
from core.scene import Dimension, Scene


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

    def _put_objects(self):
        for key, obj in self.objects.items():
            for i in range(len(obj.drawing)):
                for j in range(len(obj.drawing[0])):
                    self.map[i+obj.position.x][j +
                                               obj.position.y] = obj.drawing[i][j]

    def _draw(self):
        self._clean()
        self._put_objects()
        row = []
        for i in range(self.rows):
            column = []
            for j in range(self.columns):
                column.append(self.map[i][j])
            row.append(''.join(column))
        return '\n'.join(row)
