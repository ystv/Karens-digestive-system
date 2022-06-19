# -=[ Karen's Digestive System ]=-

# Imports ---------
#from importlib.metadata import files
#from curses import window
import tkinter as tk

# Errors ----------
def error_window(ErrorText):
    if ErrorText == "":
        ErrorText = "Unknown Error"
    ErrorWindow=tk.Tk()
    #ErrorWindow.geometry("525x240")
    ErrorWindow.resizable(False, False)
    ErrorWindow.title("Error")
    TitleText=tk.Label(ErrorWindow,text=("\n             ========================================================       \n\nError Description: "+ErrorText+"\n\nIf the problem persists, contact #computing\n\n       ========================================================\n\n\n"
                                         )).pack()
    Button=tk.Button(ErrorWindow,text="    Ok    ",command=ErrorWindow.destroy).pack()

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
        global file_types
        files_supported = "test"
        #files_supported = str(file_types).replace('[','').replace(']','').replace('\'','')
        version = "test"
        text = tk.Label(GUI,text="Karen's Digestive System (v "+version+") by Jamie",height=10,font=50,bg='#597685',fg='white')
        #text.pack(side="bottom")
        text = tk.Label(GUI,text="This is a Beta test, please report any bugs in #computing on Slack\nPlease confirm your footage is on pending edits before putting the SD card away!",height=5,font=("TkSubHeadingFont",20),bg='#597685',fg='white')
        text.pack(side="bottom")
        GUI.bind('<Return>',error_window)
        GUI.mainloop()

# Main Program
main_window()
