# Imports ---------
import tkinter as tk
import os
from subprocess import run

# Temp Variables
output = '/media/testingest'

# Variable Defaults
category = None

def enter_pressed(e):
        print("Function incomplete")

# Detect Removeable Media ------
def detect_media():
    GUI.after(500, detect_media)
    try:
        os.listdir("/media/testingest")[0]
    except:
        instruction.set("Insert SD Card or Storage Device")
    else:
        instruction.set("Storage Device Found")
        global cat_GUI
        global folder_GUI
        try:
            cat_GUI.deiconify()
        except:
            try:
                folder_GUI.deiconify()
            except:
                category_selection()

# GUI ----------
def main_window():
    global instruction
    global GUI
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
    version = "Pre-Alpha"
    text = tk.Label(GUI,text="Karen's Digestive System (v "+version+") by Jamie",height=10,font=50,bg='#597685',fg='white')
    text.pack(side="bottom")
    text = tk.Label(GUI,text="This is a Pre-Alpha Build and does not ingest footage in its current state!",height=5,font=("TkSubHeadingFont",20),bg='#597685',fg='white')
    text.pack(side="bottom")#
    #GUI.bind('<Return>',enter_pressed)
    GUI.after(500, detect_media)
    GUI.mainloop()

def category_selection():
        def select(selection):
            global category
            category = selection
        try:
            global folder_GUI
            folder_GUI.destroy()
        except:
            pass
        global cat_GUI
        cat_GUI = tk.Toplevel()
        cat_GUI.geometry("970x540")
        cat_GUI.grid_columnconfigure(0, weight=1)
        cat_GUI.grid_columnconfigure(4, weight=1)
        cat_GUI.grid_rowconfigure(6, weight=1)
        cat_GUI['background']='#597685'
        cat_GUI.title("Ingest Wizard")
        tk.Label(cat_GUI,text="\nSelect a Category:\n",height=2,font=("TkHeadingFont",30),bg='#597685').grid(column=1,row=0,columnspan=3)
        tk.Button(cat_GUI,text="Entertainment",command=lambda *args: select('Entertainment')).grid(column=1,row=1,sticky='EW') #,ipadx=10
        tk.Button(cat_GUI,text="Factual",command=lambda *args: select('Factual')).grid(column=3,row=1,sticky='EW')
        tk.Label(cat_GUI,bg='#597685').grid(row=2)
        tk.Button(cat_GUI,text="Sport",command=lambda *args: select('Sport')).grid(column=1,row=3,sticky='EW')
        tk.Button(cat_GUI,text="Commercial",command=lambda *args: select('Commercial')).grid(column=3,row=3,sticky='EW')
        tk.Label(cat_GUI,bg='#597685').grid(row=4)
        tk.Button(cat_GUI,text="Scripted",command=lambda *args: select('Scripted')).grid(column=1,row=5,sticky='EW')
        tk.Button(cat_GUI,text="Other",command=lambda *args: select('Other')).grid(column=3,row=5,sticky='EW')
        tk.Button(cat_GUI,text=" < Back ",bg='#737373',highlightbackground='#597685').grid(column=1,row=7,sticky='S',pady=20) #,padx=120 ,ipadx=5
        tk.Button(cat_GUI,text=" Next > ",command=lambda:[folder_selection(category)],highlightbackground='#597685').grid(column=3,row=7,sticky='S',pady=20)
        #cat_GUI.bind('<Return>',enter_pressed)
        cat_GUI.mainloop()

def folder_selection(category):
    global cat_GUI
    cat_GUI.destroy()
    global folder_GUI
    folder_GUI = tk.Toplevel()
    folder_GUI.geometry("970x540")
    folder_GUI['background']='#597685'
    folder_GUI.title("Ingest Wizard")
    tk.Label(folder_GUI,text="\nSelect a Production:\n",height=2,font=("TkHeadingFont",30),bg='#597685').grid(column=1,row=0,columnspan=3)
    text2 = run("ls -a "+output+" | grep -i boot", shell=True, capture_output=True).stdout
    tk.Label(folder_GUI,text=text2).grid(row=2)
    tk.Label(folder_GUI,text=category).grid(row=3)
    tk.Button(folder_GUI,text=" < Back ",command=lambda:[category_selection()],highlightbackground='#597685').grid(column=1,row=7,sticky='S',pady=20) #,padx=120 ,ipadx=5
    tk.Button(folder_GUI,text=" Next > ",command=lambda:[print('no')],highlightbackground='#597685').grid(column=3,row=7,sticky='S',pady=20)
    folder_GUI.mainloop()

main_window()
