from threading import Thread
from core.input import InputChannel
import cli.util.input as inp


class CLIInputChannel(Thread, InputChannel):
    def __init__(self, special_input_callbacks, game_over_input='q') -> None:
        Thread.__init__(self, group=None, target=self.start,
                        name='cli_input_channel', args=self, kwargs=None, daemon=None)
        InputChannel.__init__(self, special_input_callbacks)

        self._game_over_input = game_over_input

    def run(self) -> None:
        self.open()

    def open(self):
        self.current_input = None
        while self.current_input != self._game_over_input:
            try:
                self.current_input = inp.getch()
                if self.current_input in self._callbacks:
                    self._callbacks[self.current_input]()
                else:
                    self.notify_all(self.current_input)
            except:
                # ascii decode error may happen
                # no need to handle this case
                # but the program should not crash.
                pass

    def stop(self):
        # Stop the infinite loop by setting current input to game over input
        self.current_input = self._game_over_input

    def subscribe(self, game_object):
        self._subscribers[game_object.get_id()] = game_object

    def notify_all(self, key: chr):
        for subscriber in self._subscribers.values():
            subscriber.on_key_pressed(key)
