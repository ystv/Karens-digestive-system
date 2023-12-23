# Imports
import os
import threading
import time
directory = "/home/jambo/Documents/Coding/Karens-digestive-system/Test" # "/dev" Change for testing
active_removable_devices = []

if __name__ == "__main__": # Checking that this file is only being imported, not directly run
    print("Please run main.py")
    quit()

def grab_dev_dir():
    global dev_files; global dev_len
    dev_files = [file for file in os.listdir(directory)] # if file.startswith("sd")]
    dev_len = len(dev_files)

def wait_for_media():
    grab_dev_dir()
    while dev_len >= len([file for file in os.listdir(directory)]):
        if dev_len > len([file for file in os.listdir(directory)]):
            grab_dev_dir()
        pass
    for device in [file for file in os.listdir(directory)]:
        if device not in dev_files:
            active_removable_devices.append(directory+"/"+device)
            print(active_removable_devices)
        
def detect_media_thread():
    #download_thread = threading.Thread(target=wait_for_media, name="Detect Removeable Media")
    #while download_thread.is_alive() == False:
    #    download_thread.start()
    while True:
        #wait_for_media()
        download_thread = threading.Thread(target=wait_for_media, name="Detect Removeable Media")
        while download_thread.is_alive() == False:
            download_thread.start()