# -=[ Karen's Digestive System ]=-

# Imports ---------
#from importlib.metadata import files
#from curses import window
import tkinter as tk
statusWindow = __import__("status-windows") 
def enter_pressed(e):
        statusWindow.error_window("Function Incomplete")

# GUI ----------
def main_window():
        GUI = tk.Tk()
        GUI.geometry("1920x1080")
        GUI['background']='#597685'
        GUI.title("Karen's Digestive System")
        GUI.attributes("-fullscreen",True)
        Title = tk.Label(GUI,text="\nKaren the Ingest Machine\n",height=3,font=("TkHeadingFont",80),bg='#597685').pack()
        text = tk.Label(GUI,text=" ",height=2,font=25,bg='#597685').pack()
        text = tk.Label(GUI,text="Insert SD Card or Storage Device",height=2,font=("TkSubHeadingFont",25),bg='#597685').pack()
        text = tk.Label(GUI,text=" ",height=2,font=25,bg='#597685').pack()
        version = "DEV MODE"
        text = tk.Label(GUI,text="Karen's Digestive System (v "+version+") by Jamie",height=10,font=50,bg='#597685',fg='white')
        text.pack(side="bottom")
        text = tk.Label(GUI,text="This is a Beta test, please report any bugs in #computing on Slack\nPlease confirm your footage is on pending edits before putting the SD card away!",height=5,font=("TkSubHeadingFont",20),bg='#597685',fg='white')
        text.pack(side="bottom")
        GUI.bind('<Return>',enter_pressed)
        GUI.mainloop()

# Main Program
main_window()