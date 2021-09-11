from core.util.singleton import Singleton
from core.object import GameObject


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
