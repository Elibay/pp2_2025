import os
from colorama import Fore

import sys, tty, termios

# GREEN is file
# RED is directory
# Cursor is Blue

def print_files(path, cursor):
    dirs = os.listdir(path)
    i = 0
    for dir in dirs:
        if i == cursor:
            print(Fore.BLUE + dir)
        elif os.path.isdir(path + "/" + dir):
            print(Fore.RED + dir)
        else:
            print(Fore.GREEN + dir)
        i += 1

path = "../.."
cursor = 0
from pynput import keyboard
    
with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc:
            break
        os.system("clear")
        print_files(path, cursor)
        if event.key == keyboard.Key.up:
            cursor -= 1
            cursor = max(0, cursor)
        if event.key == keyboard.Key.down:
            cursor += 1
    