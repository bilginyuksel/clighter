from core.scene import Dimension, Scene


class CLIScene(Scene):
    def __init__(self, dimension: Dimension):
        super().__init__(dimension)

        self.rows, self.columns = dimension.width, dimension.height
        self.map = [[' ' for _ in range(self.columns)]
                    for _ in range(self.rows)]

    def draw(self):
        # self._clean()
        # self._put_objects()
        # move to top-left corner of the CLI
        print("\033[0;0H")
        print(self._draw())
    
    def _clean(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.map[i][j] = ' '
    
    def _put_objects(self):
        pass

    def _draw(self):
        row = []
        for i in range(self.rows):
            column = []
            for j in range(self.columns):
                column.append(self.map[i][j])
            row.append(''.join(column))
        return ''.join(row)
