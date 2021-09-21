from threading import Thread

from .util import stdin
from ..core import InputChannel


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
            self.current_input = stdin.read()
            if self.current_input == None:
                continue

            if self.current_input in self._callbacks:
                self._callbacks[self.current_input]()
            else:
                self.notify_all(self.current_input)

    def stop(self):
        # Stop the infinite loop by setting current input to game over input
        self.current_input = self._game_over_input
