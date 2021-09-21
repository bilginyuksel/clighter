from typing import List, Tuple
from .. import Dimension


def read_from_file(filepath: str) -> Tuple[List, Dimension]:
    """
    Read the game object from given file and return the `drawing` and 
    the `dimension` of the object.
    """

    with open(filepath, 'r') as f:
        lines = f.read().split('\n')
        axis_y, axis_x = len(lines), max([len(line) for line in lines])
        drawing = [[' ' for _ in range(axis_x)] for _ in range(axis_y)]

        for i in range(len(lines)):
            for j in range(len(lines[i])):
                drawing[i][j] = lines[i][j]

    return drawing, Dimension(axis_y, axis_x)
