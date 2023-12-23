# Imports
import os
import threading
import time
from removeable_media import directory

def grab_dev_dir():
    global dev_files; global dev_len
    dev_files = [file for file in os.listdir("/dev")] # if file.startswith("sd")]
    dev_len = len(dev_files)

def wait_for_media():
    global lol
    grab_dev_dir()
    while dev_len >= len([file for file in os.listdir("/dev")]):
        if dev_len > len([file for file in os.listdir("/dev")]):
            grab_dev_dir()
        pass
    for device in [file for file in os.listdir("/dev")]:
        if device not in dev_files:
            lol = directory+"/"+device
            #print(test)
            return lol