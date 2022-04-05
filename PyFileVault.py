import base64, hashlib, os, cryptography, webbrowser
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import simpledialog as sd
from tkinter import messagebox as mb

if not os.path.exists(os.getenv('APPDATA')+'\\PyFileVaultTemp'): os.mkdir(os.getenv('APPDATA')+'\\PyFileVaultTemp')
tdir = os.getenv('APPDATA')+'\\PyFileVaultTemp'

def open_url(url):
   webbrowser.open_new_tab(url)

def resource_path(relative_path):    
    try:       
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def pyv_handler(task):
    global filez, key
    filez = []
    key = ""
    if task==1 or task==2 or task==5:
        filez = list(getfilez())
    elif task==3 or task==4:
        filez = [os.path.join(dp, f) for dp, dn, fn in os.walk(getfilez(1)) for f in fn]
        if len(filez)==0: mb.showerror("Error", "Folder is empty!")
    if filez:
        key = sd.askstring("Secret Key", "Enter Secret Key:", show='*', parent=root)
        if task==1 or task==3: key2 = sd.askstring("Secret Key Confirmation", "Enter Secret Key Again:", show='*', parent=root)
        else: key2 = key
        if key and key==key2:
            key = hashlib.md5(key.encode('utf-8')).hexdigest()
            key = base64.urlsafe_b64encode(key.encode('utf-8'))
            if task==1 or task==3:
                pyv_enc(filez, key)
            elif task==2 or task==4:
                pyv_dec(filez, key)
            elif task==5:
                pyv_prev(filez, key)
        else:
            mb.showerror("Error", "Keys did not match!")
    
def getfilez(folder=0):
    if folder:
        filez = fd.askdirectory(parent=root, title='Choose folder')
    else:
        filez = fd.askopenfilenames(parent=root, title='Choose file(s)')
    return(filez)

def pyv_enc(filez, key):
    fernet = Fernet(key)
    for i in filez:
        with open(i, 'rb+') as file: original = file.read()
        encrypted = fernet.encrypt(original)
        with open(i, 'wb+') as file: file.write(encrypted)
        os.replace(i, f"{i}.pyfv")
    mb.showinfo("PyFileVault", "Encryption complete.")

def pyv_dec(filez, key):
    fernet = Fernet(key)
    for i in filez:
        if i[-5:]==".pyfv":
            with open(i, 'rb+') as file: original = file.read()
            try:
                decrypted = fernet.decrypt(original)
                with open(i, 'wb+') as file: file.write(decrypted)
                os.replace(i, i[:-5])
            except cryptography.fernet.InvalidToken:
                mb.showerror("Error", "Invalid key!")
        elif len(filez)==1:
            mb.showerror("Error", "Only .pyfv files can by decrypted.")
    mb.showinfo("PyFileVault", "Decryption complete.")

def pyv_prev(filez, key):
    fernet = Fernet(key)
    #give temp name to file and decrypt to tdir/timestamp, open folder and popup to delete files on closing

def on_closing():
    root.destroy()
    exit()

root = tk.Tk()
root.title("PyFileVault")
root.geometry("350x160+50+50")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.iconbitmap(default=resource_path('PyFileVault.ico'))

button1=tk.Button(root, text="Encrypt Files", command=lambda:pyv_handler(1), width=20)
button1.grid(row=1, column=1, padx=5, pady=5)

button2=tk.Button(root, text="Decrypt Files", command=lambda:pyv_handler(2), width=20)
button2.grid(row=1, column=2, padx=5, pady=5)

button3=tk.Button(root, text="Encrypt Folder", command=lambda:pyv_handler(3), width=20)
button3.grid(row=2, column=1, padx=5, pady=5)

button4=tk.Button(root, text="Decrypt Folder", command=lambda:pyv_handler(4), width=20)
button4.grid(row=2, column=2, padx=5, pady=5)

button5=tk.Button(root, text="Preview Files", command=lambda:pyv_handler(5), width=20, state="disabled")
button5.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

label7=tk.Label(text="PyFileVault 1.0 by DinVyapari™", fg="blue", cursor="hand2", font= ('SegoeUI 10 underline'))
label7.grid(row=4, column=1, columnspan=2, padx=5, pady=4)
label7.bind("<Button-1>", lambda e:open_url("https://github.com/DinVyapari"))

root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

root.mainloop()