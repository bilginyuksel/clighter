import platform

__running_os = platform.system().lower()
__is_unix = (__running_os == 'linux' or __running_os == 'darwin')
__is_win = (__running_os == 'windows')


if __is_unix:
    import curses

elif __is_win:
    import ctypes

    g_handle = ctypes.windll.kernel32.GetStdHandle(ctypes.c_long(-11))
else:
    raise NotImplementedError

__unix_terminal = None


def __create_terminal():
    __unix_terminal = curses.initscr()
    return __unix_terminal


def fast_print(content):
    """
    It uses terminal manipulation library to effectively print characters to terminal.
    If you use naive print function of python you will have flickering effect when you
    draw the game content to screen. So instead of naive print function use this function to print. 

    NOTE: Starts from 0,0 index at terminal. And draws via overriding other characters.
    """
    try:
        if __is_win:
            __win_fast_print(content)
        elif __is_unix:
            __unix_fast_print(content)
        else:
            raise NotImplementedError
    except:
        print('Fast print works unexpectedly! Check the terminal size and width for better experince')


def clear_cli():
    """
    Use this function to clear the terminal. Always use this function before using `fast_print`.

    NOTE: For windows it sets up the console cursor to (0,0) for unix systems it calls
    the clear function of the `curses` libraries `terminal` instance that we created.
    """
    if __is_win:
        __win_clear_cli()
    elif __is_unix:
        __unix_clear_cli()
    else:
        raise NotImplementedError


def __unix_fast_print(content):
    terminal = __unix_terminal or __create_terminal()
    terminal.addstr(0, 0, content)


def __unix_clear_cli():
    terminal = __unix_terminal or __create_terminal()
    terminal.clear()


def __win_fast_print(content):
    ctypes.windll.kernel32.WriteConsoleW(g_handle, ctypes.c_wchar_p(
        content), ctypes.c_ulong(len(content)), ctypes.c_void_p(), None)


def __win_clear_cli():
    value = 0 + (0 << 16)
    ctypes.windll.kernel32.SetConsoleCursorPosition(
        g_handle, ctypes.c_ulong(value))
