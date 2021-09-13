import platform

__running_os = platform.system().lower()

# Also the platform could be java,
# Application libraries didn't test for java,
# so we will throw `NotImplementedError` if running_os is java
__is_unix = (__running_os == 'linux' or __running_os == 'darwin')
__is_win = (__running_os == 'windows')

if __is_unix:
    import curses

elif __is_win:
    import msvcrt

else:
    raise NotImplementedError

__unix_terminal = None


def __create_terminal():
    curses.noecho()
    __unix_terminal = curses.initscr()
    __unix_terminal.nodelay(True)
    return __unix_terminal


def __unix_read() -> chr:
    # We should not initialize curses unless it is called
    unix_terminal = __unix_terminal or __create_terminal()
    try:
        return unix_terminal.getkey()
    except:
        # When there is no input to read it will throw an error
        # No need to do anything in this except block
        # We put this except block to avoid application crash
        # Return None if there is an error
        return None


def __win_read() -> chr:
    try:
        return msvcrt.getch().decode('ascii')
    except:
        # When getch captures a character which cannot decode to ascii
        # it will throw an error, no need to handle this error
        # to avoid application crash catch the error and return None
        return None


__supported_os_read_callbacks = {
    'linux': __unix_read,
    'darwin': __unix_read,
    'windows': __win_read
}


def read():
    """
    Reads the system input whenever keyboard press captured gets the character data
    and returns it immediately. If there is no input to return but still this function
    ran then it will return None
    """
    if __running_os not in __supported_os_read_callbacks:
        raise NotImplementedError

    return __supported_os_read_callbacks[__running_os]()
