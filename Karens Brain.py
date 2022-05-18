# -=[ Karen's Digestive System ]=-

# Imports ---------
#from importlib.metadata import files
import tkinter as tk
import time
import os
import shutil
import glob

print_debug_config = 'disabled'
debug_output = []
Output = r'P:/'         # Output drive
Input = [r'E:/',r'H:/'] # Input drives
file_types = ['.MTS','.mp4','.WAV','.mp3','.mkv','.mov','.avi'] # Add more video & audio file extensions here
version = '1.0.4'

# Debugging -------
#def debug(text):
#    if print_debug_config == 'enabled':
#        print(text) # add date and time stamp
#    debug_output.append(text)
    #create a config text file and a debug text file

# Errors ----------
def error_window(ErrorText):
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
    for file_type in file_types:
        files = glob.glob(source + "/**/*"+file_type, recursive = True)
        for file in files:
            shutil.copyfile(file,destination+'/'+os.path.basename(file))

def show_ingest_status_window(status):
    global ingest_status_window
    ingest_status_window = tk.Tk()
    ingest_status_window.geometry("300x200")
    ingest_status_window.title("Ingest Status")
    text = tk.Label(ingest_status_window,text="            "+status+"            \n\n ",
                        height=8).pack()
    if status == "Ingest Complete!":
        Button=tk.Button(ingest_status_window,text="    Ok, close    " , command=ingest_status_window.destroy).pack()
    

# GUI ----------
def main_window():
    try:
        GUI = tk.Tk()
        GUI.geometry("1920x1080")
        GUI.title("Karen's Digestive System")
        GUI.attributes("-fullscreen",True)
        Title = tk.Label(GUI,text="\nIngest Options\n",height=3,font=("TkHeadingFont",25)).pack()
        text = tk.Label(GUI,text="Production Folder Name (case sensitive):",height=2,font=19).pack()
        global TextEntry
        TextEntry = tk.Entry(GUI,width=50)
        TextEntry.pack()
        text = tk.Label(GUI,text=" ",height=2,font=19).pack()
        Button=tk.Button(GUI,text="Ingest" , command=confirmation_window).pack()
        text = tk.Label(GUI,text="This is a Beta test, please report any bugs in #computing on Slack\nPlease confirm your footage is on pending edits before putting the SD card away!\n\nKaren's Digestive System (v "+version+") by Jamie",height=5,font=19)
        text.pack(side="bottom")
        GUI.mainloop()
    except:
        error_window("Error with the Main Menu")

def confirmation_window():
    global confirmation_window
    confirmation_window = tk.Tk()
    confirmation_window.geometry("470x200")
    confirmation_window.title("Passive Agressive Pop Up")

    text = tk.Label(confirmation_window,text="            Have you checked that the Production Folder name you entered is correct?            \n\n ",
                        height=8).grid(row=0,columnspan=3)
    Button=tk.Button(confirmation_window,text="   Yes, Continue   " , command=lambda:[confirmation_window.destroy(),show_ingest_status_window("Ingesting..."),get_project_name()]).grid(row=1,column=0,sticky='e')
    Button=tk.Button(confirmation_window,text="    No, Cancel    " , command=confirmation_window.destroy).grid(row=1,column=2,sticky='w')
    confirmation_window.mainloop()
    
def get_project_name():
    ingest_status_window.update()
    global project_name
    project_name = TextEntry.get()
    TextEntry.delete(0,"end")
    copy_from_drives()
    
def make_import_folder():
    try:
        os.mkdir(Output+project_name)
    except:
        pass
    for i in range (1,100000):
        try:
            os.mkdir(Output+project_name+'/Import '+str(i))
        except:
            pass
        else:
            global output_path
            output_path = Output+project_name+'/Import '+str(i)
            break

def copy_from_drives():
    make_import_folder()
    try:
        copy_files(Input[0],output_path)
    except:
        pass
    else:
        make_import_folder()
    try:
        copy_files(Input[1],output_path)
    except:
        pass
    ingest_status_window.destroy()
    show_ingest_status_window("Ingest Complete!")
        
main_window()
