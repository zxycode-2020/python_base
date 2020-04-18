import tkinter
import os

from treeWindows import TreeWindows
from infoWindows import InfoWindows

win = tkinter.Tk()
win.title("sunck")
win.geometry("600x400+200+50")

path = r"C:\Users\xlg\Desktop\Python-1704"
infoWin = InfoWindows(win)
treeWin = TreeWindows(win, path, infoWin)




win.mainloop()