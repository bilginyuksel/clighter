import ctypes

g_handle = ctypes.windll.kernel32.GetStdHandle(ctypes.c_long(-11))


def fast_print(string):
    """
                Printing console will take time if you use
                python print function, to overcome cli flickering 
                problem, we need to use this function with `clear_cli`.
    """
    ctypes.windll.kernel32.WriteConsoleW(g_handle, ctypes.c_wchar_p(
        string), ctypes.c_ulong(len(string)), ctypes.c_void_p(), None)


def clear_cli():
    """
                Set cursor to (0, 0) position of the cli.
    """
    value = 0 + (0 << 16)
    ctypes.windll.kernel32.SetConsoleCursorPosition(
        g_handle, ctypes.c_ulong(value))
