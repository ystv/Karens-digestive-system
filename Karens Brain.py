# -=[ Karen's Digestive System ]=-

# Imports ---------
#from importlib.metadata import files
#from curses import window
import tkinter as tk
from tkinter import ttk,INSERT
from datetime import datetime
from datetime import date
import os
import shutil
import glob
import subprocess
CONFIG_FOLDER_PATH = r'' #\\Users\\ystv\\Documents\\DO NOT DELETE- IMPORTANT KAREN FILES\\

#try:
#    f = open('\\Users\\ystv\\Documents\\DO NOT DELETE- IMPORTANT KAREN FILES\\Projects.txt', 'x')
#    f.close()
#except:
#    pass
#with open('\\Users\\ystv\\Documents\\DO NOT DELETE- IMPORTANT KAREN FILES\\Karen Config.txt', 'r') as config_file:

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

# Config File Reading
CONFIG_FILE_PATH = CONFIG_FOLDER_PATH+'Karen Config.txt'
with open(CONFIG_FILE_PATH, 'r') as config_file:
    for line3 in config_file:
        row = line3.strip()
        if '#' not in row:
            if row[0:7] == 'Version':  version = row[10:]
            if row[0:31] == 'Print debug infomation in shell': print_debug = row[34:]
            if row[0:27] == 'Maximum project name length': MAX_CHARACTER_LENGTH = int(row[30:])
            if row[0:37] == 'Output location for production folder': Output = r''+row[40:]
            if row[0:37] == 'Input locations to search for footage':
                Input = (row[40:]).split(', ')
                Input[0] = r'' + Input[0]
                Input[1] = r'' + Input[1]
            global file_types
            if row[0:20] == 'Supported file types': file_types = (row[24:]).split(', ')
config_file.close()

# Checking input and output directories
if os.path.isdir(Input[0]) == False and os.path.isdir(Input[1]) == False:
    error_window('Input directory does not exist')
if os.path.isdir(Output) == False:
    error_window('Output directory does not exist')

# Reseting Variables
global window_open
window_open = False
progress = ''
debug_output = []
patch_notes_list = []
patch_notes_string = []

def patch_notes():
    patch_notes_window=tk.Tk()
    PATCH_NOTES_FILE_PATH = CONFIG_FOLDER_PATH+'Patch Notes.txt'
    with open(PATCH_NOTES_FILE_PATH, 'r') as patch_notes_file:
        for line2 in patch_notes_file:                
            patch_notes_list.append(line2)
    patch_notes_window.geometry('850x500')
    patch_notes_window.title("Patch Notes")
    patch_notes_window.resizable(False, False)
    patch_notes_window.grid_columnconfigure(0, weight=100)
    patch_notes_window.grid_columnconfigure(1, weight=1)
    patch_notes_window.grid_rowconfigure(1, weight=100)
    tk.Label(patch_notes_window,text=('Patch Notes:'),font=("TkHeadingFont",25)).grid(row=0,column=0,columnspan=1)

    text = tk.Text(patch_notes_window)
    for patch_note in patch_notes_list:
        text.insert(INSERT,patch_note)
    scrollbar = ttk.Scrollbar(patch_notes_window, orient='vertical', command=text.yview)
    scrollbar.grid(row=1, column=1, sticky='ns')
    text['yscrollcommand'] = scrollbar.set
    text.place(width=800, height=400, y = 50, x = 15)
    tk.Button(patch_notes_window,text="    Ok, close    ",command=patch_notes_window.destroy).grid(sticky='s',row=3,column=0,columnspan=1,pady=10)

# Debugging -------
#def debug(text):
#    if print_debug_config == 'enabled':
#        print(text) # add date and time stamp
#    debug_output.append(text)
    #create a config text file and a debug text file

# Copying Script ---
def copy_files(source,destination):
    for file_type in file_types:
        files = glob.glob(source + "/**/*"+file_type, recursive = True)
        file_count = 0
        file_count_max = len(files)
        if files != []:
            for file in files:
                file_count = file_count +1
                global progress
                global progress_text
                progress = 'Copying '+os.path.basename(file)+' from \"'+file+'\" to \"'+destination+'/'+os.path.basename(file)+'\"\n\n(File: '+str(file_count)+' of '+str(file_count_max)+')'
                progress_text['text']="            "+ingest_status+"            \n\n"+progress
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
#    try:
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
        global file_types
        files_supported = str(file_types).replace('[','').replace(']','').replace('\'','')
        text = tk.Label(GUI,text="Supported File Extensions: "+files_supported+"\nIf you think another file type should be supported, contact #computing\n\n\n\n\n\nKaren's Digestive System (v "+version+") by Jamie",height=10,font=50,bg='#597685',fg='white')
        text.pack(side="bottom")
        text = tk.Label(GUI,text="This is a Beta test, please report any bugs in #computing on Slack\nPlease confirm your footage is on pending edits before putting the SD card away!",height=5,font=("TkSubHeadingFont",20),bg='#597685',fg='white')
        text.pack(side="bottom")
        GUI.bind('<Return>',enter_pressed)
        GUI.mainloop()
#    except:
#        error_window("Error with the Main Menu")

def reset_window_open():
    global window_open
    window_open = False

def enter_pressed(e):
    show_confirmation_window()

def show_confirmation_window():
    global window_open
    if window_open == False:
        global project_name
        project_name = TextEntry.get()
        if '.' in project_name or '\\' in project_name or '/' in project_name or ':' in project_name or '*' in project_name or '"' in project_name or '<' in project_name or '>' in project_name or '|' in project_name or '?' in project_name:
            error_window('This project name is not supported\nA folder can not contain the following characters:\n. \\ / : * " < > |')
            TextEntry.delete(0,"end")
        elif project_name.isspace() == True or project_name == '':
            error_window('This project name is not supported\nA folder must contain text')
            TextEntry.delete(0,"end")
        elif len(project_name) > MAX_CHARACTER_LENGTH:
            error_window('This project name is not supported\nThe maximum character limit is 50')
            TextEntry.delete(0,"end")
        else:
            window_open = True
            global confirmation_window
            confirmation_window = tk.Tk()
            confirmation_window.geometry("470x200")
            confirmation_window.resizable(False, False)
            confirmation_window.title("Passive Agressive Pop Up")
            text = tk.Label(confirmation_window,text="            Have you checked that the Production Folder name you entered is correct?            \n\n ",
                                height=8).grid(row=0,columnspan=3)
            Button=tk.Button(confirmation_window,text="   Yes, Continue   " , command=lambda:[confirmation_window.destroy(),get_project_name(),reset_window_open()]).grid(row=1,column=0,sticky='e')
            Button=tk.Button(confirmation_window,text="    No, Cancel    " , command=lambda:[confirmation_window.destroy(),reset_window_open()]).grid(row=1,column=2,sticky='w')
            confirmation_window.mainloop()
    
def get_project_name():
    TextEntry.delete(0,"end")
    copy_from_drives()
    
def make_import_folder():
    try:
        os.mkdir(Output+project_name)
    except:
        pass
    for i in range (1,100000): # DO TO: make while loop with incrementing i value
        try:
            os.mkdir(Output+project_name+'/Import '+str(i))
        except:
            pass
        else:
            global output_path
            output_path = Output+project_name+'/Import '+str(i)
            break

def copy_from_drives():
    i,num_filetypes_not_found = 0,0
    for input_num in range(0,2):
        for file_type in file_types:
            files = glob.glob(Input[input_num] + "/**/*"+file_type, recursive = True)
            i = i + 1
            if files == []:
                num_filetypes_not_found = num_filetypes_not_found + 1
    if os.path.isdir(Input[0]) == False and os.path.isdir(Input[1]) == False:
        error_window('Input directory does not exist')
    elif os.path.isdir(Output) == False:
        error_window('Output directory does not exist')
    elif num_filetypes_not_found == i:
        error_window('No supported files in input directories')
    else:
        make_import_folder()
        show_ingest_status_window("Ingesting...")
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
        output_folder_path = (Output + project_name).replace('/','\\')
        subprocess.Popen('explorer "'+output_folder_path+'"')
        show_ingest_status_window("Ingest Complete!")
        PROJECT_LIST_FILE_PATH = CONFIG_FOLDER_PATH+'Projects.txt'
        try:
            f = open(PROJECT_LIST_FILE_PATH, 'x')
            f.close()
        except:
            pass
        with open(PROJECT_LIST_FILE_PATH, 'a') as f:
            now = datetime.now()
            today = date.today()
            time_and_date = today.strftime('%d/%b/%Y')+' - '+now.strftime('%H:%M:%S')
            f.write(time_and_date+' |   '+project_name+'\n')
            f.close()

patch_notes()     
main_window()
