# Imports
import os
import threading

def grab_dev_dir():
    global dev_files; global dev_len
    dev_files = [file for file in os.listdir("/dev")] # if file.startswith("sd")]
    dev_len = len(dev_files)

def wait_for_media():
    grab_dev_dir()
    while dev_len >= len([file for file in os.listdir("/dev")]):
        if dev_len > len([file for file in os.listdir("/dev")]):
            grab_dev_dir()
        pass
    for device in [file for file in os.listdir("/dev")]:
        if device not in dev_files:
            return "/dev/"+device
        
def detect_media_thread():
    #download_thread = threading.Thread(target=wait_for_media, name="Detect Removeable Media")
    #while download_thread.is_alive() == False:
    #    download_thread.start()
    while True:
        wait_for_media()