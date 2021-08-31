import keyboard


def callback(e: keyboard.KeyboardEvent):
    print(e)


keyboard.hook(callback)
keyboard.wait(hotkey='q')
