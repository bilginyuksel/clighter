from util.collections import CircularLinkedList


class AnimationMixin:
    def __init__(self) -> None:
        self._animation_groups: dict[str, CircularLinkedList] = {}
        self._current_group: CircularLinkedList = None
        self._frame_count = 0
        self._frame_threshold = None

    def apply(self, group, fps=60):
        if not group in self._animation_groups:
            # There is no animation groups to apply
            return None
        drawings = self._animation_groups[group]
        self._current_group = drawings
        self._frame_threshold = fps / len(drawings)

    def animate(self):
        # execute the animate function per frame
        self._frame_count += 1
        if self._frame_count == self._frame_threshold and self._current_group is not None:
            self._current_group.next()
            self._frame_count = 0
