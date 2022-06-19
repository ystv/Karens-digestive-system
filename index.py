import os
import tkinter as tk

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
    print("Success")
else:
    print("Error: Required Files Missing")