from collections import defaultdict
from core.dimension import Dimension
from core.util.collections import CircularLinkedList


class AnimationFrame:
    def __init__(self, filepath, active_frame=30) -> None:
        self.frame = filepath
        self.active_frame = active_frame

        with open(filepath, 'r') as f:
            lines = f.read().split('\n')
            axis_y, axis_x = len(lines), max(
                [len(line) for line in lines])
            self.dimension = Dimension(axis_y, axis_x)
            self.frame = [
                [' ' for _ in range(axis_x)] for _ in range(axis_y)]
            for i in range(len(lines)):
                for j in range(len(lines[i])):
                    self.frame[i][j] = lines[i][j]


class AnimationMixin:
    def __init__(self) -> None:
        self._animation_groups = defaultdict(CircularLinkedList)
        self._curr_animation_group = None
        self._curr_node = None

    def anim_update(self):
        if self._curr_node is None:
            return

        self._curr_node.value.active_frame -= 1
        if self._curr_node.value.active_frame <= 0:
            # TOOD: Active frame should be dynamic
            self._curr_node.value.active_frame = 30
            self._curr_node = self._curr_animation_group.next()

        self.drawing = self._curr_node.value.frame
        self.dimension = self._curr_node.value.dimension

    def add_animation(self, group: str, animation: AnimationFrame):
        animation_group = self._animation_groups[group]
        animation_group.append(animation)

    def animate(self, group):
        if not group in self._animation_groups:
            # There is no animation groups to apply
            return None

        if self._curr_node is None:
            self._curr_animation_group = self._animation_groups[group]
            self._curr_node = self._curr_animation_group.next()
