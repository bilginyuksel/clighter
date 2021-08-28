from threading import Thread
from core.input import InputChannel
import msvcrt


class CLIInputChannel(Thread, InputChannel):
    def __init__(self, special_input_callbacks) -> None:
        Thread.__init__(self, group=None, target=self.start,
                        name='cli_input_channel', args=self, kwargs=None, daemon=None)
        InputChannel.__init__(self, special_input_callbacks)

    def run(self) -> None:
        self.open()

    def open(self):
        while self._input != 'q':
            self._input = msvcrt.getch().decode('ascii')
            if self._input in self._callbacks:
                self._callbacks[self._input]()
            else:
                self.notify_all(self._input)

    def subscribe(self, game_object):
        self._subscribers[game_object.get_id()] = game_object

    def notify_all(self, key: chr):
        for subscriber in self._subscribers.values():
            subscriber.on_key_pressed(key)

    def get_input(self):
        current_input = self._input
        self._input = None
        return current_input
