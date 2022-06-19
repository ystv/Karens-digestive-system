#imports
import tkinter as tk

# Error Windows ----------
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