import time
import pyautogui
import winsound
import os,sys
import tkinter as tk
from PIL import Image, ImageTk
run=0
def resource_path(relative_path): # prosarmozei to path pou tha valei tis eikones kai tous hxous
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
def updateImg(imgNum,duration):
    img=("Pyrus"
         "")+ str(imgNum) + ".png"
    i=Image.open(resource_path(img)).resize((win.winfo_screenwidth(), win.winfo_screenheight()),Image.LANCZOS)
    bg2=ImageTk.PhotoImage(i)
    bglbl.configure(image=bg2)
    bglbl.image=bg2
    win.update()
    time.sleep(duration)

def virus(event):
    global run
    if run==0:
        run=1
        updateImg(1,3)
        updateImg(2,3)
        updateImg(3, 3)
        updateImg(4, 3)
        updateImg(5, 3)
        updateImg(6, 3)
        updateImg(7, 3)
def disable():
    pass

time.sleep(1)

pyautogui.hotkey("win","d")

dir=os.path.dirname(os.path.abspath(sys.argv[0]))
print(dir)
time.sleep(1)
im=pyautogui.screenshot("desktop.png")
win=tk.Tk()
win.geometry("{}x{}+0+0".format(win.winfo_screenwidth(),win.winfo_screenheight()))
bg=tk.PhotoImage(file="desktop.png")
bglbl=tk.Label(win,image=bg,width=win.winfo_screenwidth(),height=win.winfo_screenheight())
bglbl.place(x=0,y=0,width=win.winfo_screenwidth(),height=win.winfo_screenheight())
bglbl.bind('<Button-1>',virus)
win.attributes("-fullscreen",True)
win.attributes("-topmost",True)
win.bind('<Escape>', disable)
win.protocol("WM_DELETE_WINDOW", disable)
win.update()


win.mainloop()