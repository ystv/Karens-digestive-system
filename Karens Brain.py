# -=[ Karen's Digestive System ]=-

# Imports ---------
#from importlib.metadata import files
#from curses import window
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
version = '1.0.7'
global window_open
window_open = False
progress = ''

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
        file_count = 0
        file_count_max = len(files)
        for file in files:
            file_count = file_count +1
            global progress
            global progress_text
            progress = 'Copying '+os.path.basename(file)+' from \"'+file+'\" to \"'+destination+'/'+os.path.basename(file)+'\"\n\n(File: '+str(file_count)+' of '+str(file_count_max)+')'
            progress_text['text']="            "+ingest_status+"            \n\n"+progress
            print(6*len(progress))
            if 6*len(progress) > 500:
                geometry = str(6*len(str(progress)))+'x200'
            else:
                geometry = '500x200'
            ingest_status_window.geometry(geometry)
            ingest_status_window.update()
            shutil.copyfile(file,destination+'/'+os.path.basename(file))

def show_ingest_status_window(status):
    global ingest_status
    ingest_status = status
    global ingest_status_window
    ingest_status_window = tk.Tk()
    ingest_status_window.title("Ingest Status")
    global progress_text
    progress_text = tk.Label(ingest_status_window,text="            "+status+"            \n\n\n"+progress,height=8)
    progress_text.pack()
    if status == "Ingest Complete!":
        Button=tk.Button(ingest_status_window,text="    Ok, close    " , command=ingest_status_window.destroy).pack()
    ingest_status_window.geometry('300x200')
    

# GUI ----------
def main_window():
    try:
        GUI = tk.Tk()
        GUI.geometry("1920x1080")
        #bg = tk.PhotoImage(file = "Marks.png")
        #label1 = tk.Label( GUI, image = bg)
        #label1.place(x = 0, y = 0)
        GUI['background']='#597685'
        GUI.title("Karen's Digestive System")
        GUI.attributes("-fullscreen",True)
        Title = tk.Label(GUI,text="\nKaren the Ingest Machine\n",height=3,font=("TkHeadingFont",80),bg='#597685').pack()
        text = tk.Label(GUI,text="Production Folder Name (case sensitive):",height=2,font=("TkSubHeadingFont",25),bg='#597685').pack()
        #GUI.wm_attributes("-transparentcolor",'#597685')
        global TextEntry
        TextEntry = tk.Entry(GUI,width=50,font=50)
        TextEntry.pack()
        text = tk.Label(GUI,text=" ",height=2,font=25,bg='#597685').pack()
        Button=tk.Button(GUI,text="Ingest" ,font=25 ,command=show_confirmation_window).pack()
        #text_bottom = "Supported File Extensions: "+file_types+"\nIf you think another file type should be supported, contact #computing\n\n"
        files_supported = str(file_types).replace('[','').replace(']','').replace('\'','')
        text = tk.Label(GUI,text="Supported File Extensions: "+files_supported+"\nIf you think another file type should be supported, contact #computing\n\n\n\n\n\nKaren's Digestive System (v "+version+") by Jamie",height=10,font=50,bg='#597685',fg='white')
        text.pack(side="bottom")
        text = tk.Label(GUI,text="This is a Beta test, please report any bugs in #computing on Slack\nPlease confirm your footage is on pending edits before putting the SD card away!",height=5,font=("TkSubHeadingFont",20),bg='#597685',fg='white')
        text.pack(side="bottom")
        GUI.bind('<Return>',enter_pressed)
        GUI.mainloop()
    except:
        error_window("Error with the Main Menu")

def reset_window_open():
    global window_open
    window_open = False

def enter_pressed(e):
    show_confirmation_window()
def show_confirmation_window():
    global window_open
    if window_open == False:
        window_open = True
        global confirmation_window
        confirmation_window = tk.Tk()
        confirmation_window.geometry("470x200")
        confirmation_window.title("Passive Agressive Pop Up")
        text = tk.Label(confirmation_window,text="            Have you checked that the Production Folder name you entered is correct?            \n\n ",
                            height=8).grid(row=0,columnspan=3)
        Button=tk.Button(confirmation_window,text="   Yes, Continue   " , command=lambda:[confirmation_window.destroy(),show_ingest_status_window("Ingesting..."),get_project_name(),reset_window_open()]).grid(row=1,column=0,sticky='e')
        Button=tk.Button(confirmation_window,text="    No, Cancel    " , command=lambda:[confirmation_window.destroy(),reset_window_open()]).grid(row=1,column=2,sticky='w')
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
    if os.path.isdir(Input[0]) == True:
        copy_files(Input[0],output_path)
        if os.path.isdir(Input[1]) == True:
            make_import_folder()
            copy_files(Input[1],output_path)
    else:
        copy_files(Input[1],output_path)

    ingest_status_window.destroy()
    global progress
    progress = ''
    show_ingest_status_window("Ingest Complete!")
        
main_window()
