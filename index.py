import os
import tkinter as tk
statusWindow = __import__("status-windows")
karensBrain = __import__("karens-brain")

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