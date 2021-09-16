from .util import Singleton
from .object import GameObject


class InputChannel(metaclass=Singleton):
    def __init__(self, special_input_callbacks) -> None:
        self._input = None
        self._callbacks = special_input_callbacks
        self._subscribers = {}

    def open(self):
        raise NotImplementedError()

    def subscribe(self, obj: GameObject):
        raise NotImplementedError()

    def notify_all(self):
        raise NotImplementedError()

    def remove(self, obj: GameObject):
        if obj.get_id() in self._subscribers:
            del self._subscribers[obj.get_id()]
