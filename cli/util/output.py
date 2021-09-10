windows = True
# try:
#     import cli.util.windows as windows
# except ImportError:
#     windows = False
#     import cli.util.unix as unix
windows = False
import cli.util.unix as unix

def fast_print(content):
    if windows:
        windows.fast_print(content)
    else:
        unix.fast_print(content)

def clear_cli():
    if windows:
        windows.clear_cli()
    else:
        unix.clear_cli()