from .util import Singleton
from .object import GameObject


class InputChannel(metaclass=Singleton):
    def __init__(self, special_input_callbacks) -> None:
        self._input = None
        self._callbacks = special_input_callbacks
        self._subscribers = {}

    def open(self):
        raise NotImplementedError()

    def subscribe(self, game_object: GameObject):
        """
        Subscribe to input channel with a game object.
        When a game object subscribed to the input channel it will 
        receive every keystroke from the user.
        """
        self._subscribers[game_object.get_id()] = game_object

    def notify_all(self, key: chr):
        """
        NotifyAll whenever a keystroke captured notify all of the subscribers. 
        Subscribers should have `on_key_pressed` method.
        """
        for subscriber in self._subscribers.values():
            subscriber.on_key_pressed(key)

    def remove(self, obj: GameObject):
        """
        Remove a subscriber from the channel. After removal subscriber should not be
        able to listen keystroke events. 
        """
        if obj.get_id() in self._subscribers:
            del self._subscribers[obj.get_id()]
