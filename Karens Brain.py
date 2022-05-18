# -=[ Karen's Digestive System ]=-

# Imports ---------
from importlib.metadata import files
import tkinter as tk
import time
import os
import shutil
import glob

print_debug_config = 'enabled'
debug_output = []

# Debugging -------
def debug(text):
    if print_debug_config == 'enabled':
        print(text) # add date and time stamp
    debug_output.append(text)
    #create a config text file and a debug text file

# Errors ----------
def ErrorMessage(ErrorText):
    # Error codes:
    if ErrorText == "":
        ErrorText = "Unknown Error"
    ErrorWindow=tk.Tk()
    ErrorWindow.geometry("525x230")
    ErrorWindow.title("Error")
    TitleText=tk.Label(ErrorWindow,text=("\n             ========================================================       \n\nError Description: "+ErrorText+"\n\nManually Ingest and Contact #computing on slack\n\n       ========================================================\n\n\n\n"
                                         )).grid(row=0,columnspan=10)
    Button=tk.Button(ErrorWindow,text="    Ok    ",command=ErrorWindow.destroy).grid(row=3,column=8,sticky='e')
    Button=tk.Button(ErrorWindow,text="   Quit   ",command=quit).grid(row=3,column=9,sticky='w')

# Copying Script ---
def copy_files(source,destination):
    files = glob.glob(source + "/**/*.MTS", recursive = True)
    print(files)
    #print(destination)
    for file in files:
        #print(file+'\n'+destination+os.path.basename(file))
        shutil.copyfile(file,destination+'/'+os.path.basename(file))

# GUIs ----------
def StartMenu():
    try:
        GUI = tk.Tk()
        GUI.geometry("1920x1080")
        GUI.title("Karen's Digestive System")

        Title = tk.Label(GUI,text="\nIngest Options\n",height=3,font=("TkHeadingFont",25)).pack()
        text = tk.Label(GUI,text="Production Folder Name (for drive):",height=2,font=19).pack()

        global TextEntry
        TextEntry = tk.Entry(GUI,width=50)
        TextEntry.pack()
        text = tk.Label(GUI,text=" ",height=2,font=19).pack()
        
        Button=tk.Button(GUI,text="Ingest" , command=popup1).pack()
        GUI.mainloop()
    except:
        ErrorMessage("Error with the Main Menu")
    
        
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
    project_name = TextEntry.get()
    print(project_name)
    Output = r'P:/'
    Input1 = r'H:/'
    #file_found = False
    #for file in os.listdir(Output):
    #    if os.path.isfile(Output+project_name) == True:
    #        file_found = True
    #        break
    #    pass
    #if file_found == False:
    #    os.mkdir(Output+project_name)
    #file_found = True
    try:
        os.mkdir(Output+project_name)
    except:
        pass
    else:
        pass
    Output = Output+project_name
    copy_files(Input1,Output)

    #ErrorMessage("This function is incomplete")

    
    
StartMenu()
#InfoEntered()
