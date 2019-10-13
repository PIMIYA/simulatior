from pynput.mouse import Listener, Button


def on_move(x, y):
    return
    print('Pointer moved to {0}'.format(
        (x, y)))


def on_click(x, y, button, pressed):
    if pressed:
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
    if button == Button.right:
        # Stop listener
        return False


def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))


# Collect events until released
with Listener(
        on_move=on_move,
        on_click=on_click) as listener:
    listener.join()
