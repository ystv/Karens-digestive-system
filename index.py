import os
import tkinter as tk
import time
statusWindow = __import__("status-windows")
karensBrain = __import__("karens-brain")
loop = True

# Checking for required files

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return True
        else:
            return False

if (
    find("Karen Config.txt",os.getcwd()) == True,
    find("Karens Brain.py",os.getcwd()) == True
):
    karensBrain.main_window()
else:
    statusWindow.error_window("Required Files Missing")

# Detect Removeable Media

def detect_media():
    global loop
    while loop == True:
        time.sleep(1)
        if os.system("ls /media | grep sd >/dev/null 2>&1") == 0:
            # add next window here
            karensBrain.instruction.set("SD Found")
detect_media()