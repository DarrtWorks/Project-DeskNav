from cgitb import text
import subprocess
import tkinter
import webbrowser
from tkinter import *
import ctypes as ct
import os


def submit():
  n = entry.get()
  if n=="notepad":
    subprocess.call('notepad.exe')
    
  elif n=="youtube":
     webbrowser.open('https://youtube.com')

  elif n =="vscode":
   subprocess.Popen('C:\\Users\\Darsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')
  elif n =="pythonex":
    os.startfile('C:\\Users\\Darsh\\OneDrive\\Desktop\\Pythonex')
  elif n=="whatsapp":
    webbrowser.open('https://web.whatsapp.com')  
  elif n=="src_file":
    os.startfile('C:\\Users\\Darsh\\OneDrive\\Desktop\\Pythonex\\Programs\\SubProcess.txt')

def dark_title_bar(window):
    """
    MORE INFO:
    https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value),
                         ct.sizeof(value))

canvas = Tk()
canvas.title("Prompt")
canvas.geometry("400x100")
canvas.maxsize(400,100)
canvas.minsize(400,100)
canvas.config(bg = '#423f3f')
logo = PhotoImage(file ='C:\\Users\\Darsh\\OneDrive\\Desktop\\Pythonex\\Programs\\log.png')
canvas.iconphoto(False,logo)
dark_title_bar(canvas)
canvas.wm_attributes("-topmost",True)
entry = Entry()
entry.place(relx=.5, rely=.5,anchor= CENTER)

entry.config(bd =2)
entry.config(font = ('Cascadia Mono',15))
entry.config(bg = '#423f3f')
entry.config(fg = 'White')
submit = Button(canvas,text="Open",command=submit,bg='#272727',fg='WHITE',bd=2)
submit.place(relx=.5, rely=0.85,anchor=CENTER)
canvas.mainloop()

