# imports
import removeable_media
from removeable_media import *
import time

if __name__ == "__main__":
    test = []
    removeable_media.detect_media_thread()
    while True:
        print(test)
        time.sleep(1)