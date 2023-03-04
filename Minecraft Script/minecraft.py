from curses import window
from wave import Wave_write
import pyautogui
import sys
import threading
from pynput.keyboard import Listener, KeyCode
import time
import os

start_stop_key = KeyCode(char='=')
start_key = KeyCode(char='-')

def walk():
    # pyautogui.keyDown('w')
    # pyautogui.mouseDown(button='right')
    pyautogui.mouseDown()
    threading.Timer(1, walk).start()

# walk()

def on_press(key):
    if key == start_stop_key:
        exit()
    elif key == start_key:
        walk()

with Listener(on_press=on_press) as listener:
    listener.join()