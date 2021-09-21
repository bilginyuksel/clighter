from collections import defaultdict
from .util import CircularLinkedList, read_from_file


class AnimationFrame:
    def __init__(self, filepath, active_frame=30) -> None:
        self.active_frame = active_frame
        self.frame, self.dimension = read_from_file(filepath)


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
        """
        Add animations for specific groups.
        Animation groups can be executed consecutively. So use this function
        to define consecutive animations for a specific action. 
        """
        animation_group = self._animation_groups[group]
        animation_group.append(animation)

    def animate(self, group):
        """
        Use this function to start an animation group action.
        It will find the given `group` animations and execute consecutively.
        """
        if not group in self._animation_groups:
            # There is no animation groups to apply
            return None

        if self._curr_node is None:
            self._curr_animation_group = self._animation_groups[group]
            self._curr_node = self._curr_animation_group.next()
