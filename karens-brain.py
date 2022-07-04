# -=[ Karen's Digestive System ]=-

# Imports ---------
import tkinter as tk
import time
import os
statusWindow = __import__("status-windows")

def enter_pressed(e):
        statusWindow.error_window("Function Incomplete")

# Detect Removeable Media ------
def detect_media():
    global loop
    while loop == True:
        time.sleep(1)
        if os.system("ls /media | grep sd >/dev/null 2>&1") != "":
            # add next window here
            instruction.set("SD Found")

# GUI ----------
def main_window():
        global instruction
        GUI = tk.Tk()
        instruction = tk.StringVar()
        instruction.set("Insert SD Card or Storage Device")
        GUI.geometry("1920x1080")
        GUI['background']='#597685'
        GUI.title("Karen's Digestive System")
        GUI.attributes("-fullscreen",True)
        title = tk.Label(GUI,text="\nKaren the Ingest Machine\n",height=3,font=("TkHeadingFont",80),bg='#597685').pack()
        text = tk.Label(GUI,text=" ",height=2,font=25,bg='#597685').pack()
        instruction_label = tk.Label(GUI,textvariable=instruction,height=2,font=("TkSubHeadingFont",25),bg='#597685')
        instruction_label.pack()
        text = tk.Label(GUI,text=" ",height=2,font=25,bg='#597685').pack()
        version = "DEV MODE"
        text = tk.Label(GUI,text="Karen's Digestive System (v "+version+") by Jamie",height=10,font=50,bg='#597685',fg='white')
        text.pack(side="bottom")
        text = tk.Label(GUI,text="This is a Beta test, please report any bugs in #computing on Slack\nPlease confirm your footage is on pending edits before putting the SD card away!",height=5,font=("TkSubHeadingFont",20),bg='#597685',fg='white')
        text.pack(side="bottom")#
        GUI.bind('<Return>',enter_pressed)
        GUI.after(0, detect_media)
        GUI.mainloop()