import os
import cryptography as crypt
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import simpledialog as sd
from tkinter import messagebox as mb

if not os.path.exists(os.getenv('APPDATA')+'\\PyFileVaultTemp'): os.mkdir(os.getenv('APPDATA')+'\\PyFileVaultTemp')
tdir = os.getenv('APPDATA')+'\\PyFileVaultTemp'

def pyv_handler(task):
    global filez, key
    filez = []
    key = ""
    if task==1 or task==2 or task==5:
        filez = list(getfilez())
    elif task==3 or task==4:
        filez = [os.path.join(dp, f) for dp, dn, fn in os.walk(getfilez(1)) for f in fn]
        if len(filez)==0: mb.showinfo("Error", "Folder is empty!")
    if filez: key = sd.askstring("Secret Key", "Enter Secret Key:", show='*', parent=root)
    if key:
        print(filez, key)
    
def getfilez(folder=0):
    if folder:
        filez = fd.askdirectory(parent=root, title='Choose folder')
    else:
        filez = fd.askopenfilenames(parent=root, title='Choose file(s)')
    return(filez)

def pyv_enc(filez, key):
    pass

def pyv_dec(filez, key):
        pass

def pyv_prev(filez, key):
    #give temp name to file and decrypt to temp, then launch
    pass

def on_closing():
    root.destroy()
    exit()

root = tk.Tk()
root.title("PyFileVault")
root.geometry("350x160+50+50")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.iconbitmap(default='./PyFileVault.ico')

button1=tk.Button(root, text="Encrypt Files", command=lambda:pyv_handler(1), width=20)
button1.grid(row=1, column=1, padx=5, pady=5)

button2=tk.Button(root, text="Decrypt Files", command=lambda:pyv_handler(2), width=20)
button2.grid(row=1, column=2, padx=5, pady=5)

button3=tk.Button(root, text="Encrypt Folder", command=lambda:pyv_handler(3), width=20)
button3.grid(row=2, column=1, padx=5, pady=5)

button4=tk.Button(root, text="Decrypt Folder", command=lambda:pyv_handler(4), width=20)
button4.grid(row=2, column=2, padx=5, pady=5)

button5=tk.Button(root, text="Preview Files", command=lambda:pyv_handler(5), width=20)
button5.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

label7=tk.Label(text="PyFileVault 1.0 by DinVyapari™")
label7.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

root.mainloop()