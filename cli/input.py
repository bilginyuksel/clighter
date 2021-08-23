import msvcrt
from typing import Callable


class CLIInputChannel:
    def __init__(self, special_input_callbacks) -> None:
        self._input = None
        self._callbacks = special_input_callbacks

    def open(self):
        while self._input != 'q':
            self._input = msvcrt.getch().decode('ascii')
            print(self._input)
            if self._input in self._callbacks:
                self._callbacks[self._input]()

    def get_input(self):
        current_input = self._input
        self._input = None
        return current_input
