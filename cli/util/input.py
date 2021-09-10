windows = True
window = None
try:
    import msvcrt
except ImportError:
    windows = False
    import curses
    curses.noecho()
    window= curses.initscr()
    window.nodelay(True)

def getch():
    if windows:
        return msvcrt.getch()
    else:
        return window.getkey()

