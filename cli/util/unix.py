import curses

terminal = curses.initscr()

def fast_print(content):
    terminal.addstr(0, 0, content)


def clear_cli():
    terminal.clear()