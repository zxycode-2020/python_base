import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+200+20")

#菜单条
menubar = tkinter.Menu(win)

#菜单
menu = tkinter.Menu(menubar, tearoff=False)
for item in ["Python", "C", "C++", "OC", "Swift", "C#", "shell", "Java", "JS", "PHP", "汇编", "NodeJS", "退出"]:
    menu.add_command(label=item)

menubar.add_cascade(label="语言", menu=menu)

def showMenu(event):
    menubar.post(event.x_root, event.y_root)
win.bind("<Button-3>", showMenu)


win.mainloop()