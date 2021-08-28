from threading import Thread
from core.input import InputChannel
import msvcrt


class CLIInputChannel(Thread, InputChannel):
    def __init__(self, special_input_callbacks, game_over_input='q') -> None:
        Thread.__init__(self, group=None, target=self.start,
                        name='cli_input_channel', args=self, kwargs=None, daemon=None)
        InputChannel.__init__(self, special_input_callbacks)

        self._game_over_input = game_over_input

    def run(self) -> None:
        self.open()

    def open(self):
        current_input = None
        while current_input != self._game_over_input:
            try:
                current_input = msvcrt.getch().decode('ascii')
                if current_input in self._callbacks:
                    self._callbacks[current_input]()
                else:
                    self.notify_all(current_input)
            except:
                # ascii decode error may happen
                # no need to handle this case
                # but the program should not crash.
                pass

    def subscribe(self, game_object):
        self._subscribers[game_object.get_id()] = game_object

    def notify_all(self, key: chr):
        for subscriber in self._subscribers.values():
            subscriber.on_key_pressed(key)
