# -=[ Karen's Digestive System ]=-

# Imports ---------
import tkinter as tk
import time
import os
import shutil
# -----------------

# Errors ----------
def ErrorMessage(ErrorNum):
    # Error Number Key:
    x = ErrorNum
    if x == "001":
        ErrorText = "This function is incomplete"
    elif x == "002":
        ErrorText = "Error with the Main Menu"
    else:
        ErrorText = "Unknown Error"
    ErrorWindow=tk.Tk()

    ErrorWindow.geometry("525x230")

    ErrorWindow.title("Error")

    TitleText=tk.Label(ErrorWindow,text=("\n             ========================================================       \n\nError "+ErrorNum+": "+ErrorText+"\n\nManually Ingest and Contact #computing on slack\n\n       ========================================================\n\n\n\n"
                                         )).grid(row=0,columnspan=10)
    Button=tk.Button(ErrorWindow,text="    Ok    ",command=ErrorWindow.destroy).grid(row=3,column=8,sticky='e')
    Button=tk.Button(ErrorWindow,text="   Quit   ",command=quit).grid(row=3,column=9,sticky='w')
# -----------------

def StartMenu():
    try:
        GUI = tk.Tk()
        GUI.geometry("1920x1080")

        GUI.title("Karen's Digestive System")

        Title = tk.Label(GUI,text="\nIngest Options\n",height=3,font=("TkHeadingFont",25)).pack()
        text = tk.Label(GUI,text="Production Folder Name (for drive):",height=2,font=19).pack()

        global test
        test = str()
        TextEntry = tk.Entry(GUI,width=50,textvariable=test).pack()
        print(TextEntry)
        text = tk.Label(GUI,text=" ",height=2,font=19).pack()

        
        

        Button=tk.Button(GUI,text="Ingest" , command=popup1).pack()
        #Button=tk.Button(GUI,text="Quit Program" , command=quit).pack() # Why would you want to quit the program? Let's patch that

        #entry.delete(0, tk.END)
        GUI.mainloop()
    except:
        ErrorMessage("002")
    
        
def popup1():
    popup1 = tk.Tk()
    popup1.geometry("470x200")
    popup1.title("Passive Agressive Pop Up")

    text = tk.Label(popup1,text="            Have you checked that the Production Folder name you entered is correct?            \n\n ",
                        height=8).grid(row=0,columnspan=3)

    Button=tk.Button(popup1,text="   Yes, Continue   " , command=InfoEntered).grid(row=1,column=0,sticky='e')
    Button=tk.Button(popup1,text="    No, Cancel    " , command=popup1.destroy).grid(row=1,column=2,sticky='w')
    
    popup1.mainloop()

def InfoEntered():
    ErrorMessage('001')
    #Input1 = r"C:\Users\Jamie\Desktop\"
    #Input2 = r"E:
    #output
    print(test)
    bruh = TextEntry.get()
    print(bruh)
    
    
StartMenu()
