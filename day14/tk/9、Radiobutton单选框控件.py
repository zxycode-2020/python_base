import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+200+20")

def updata():
    print(r.get())

#一组单选框要绑定同一个变量
r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win, text="one", value=44, variable=r, command=updata)
radio1.pack()
radio2 = tkinter.Radiobutton(win, text="two", value=55, variable=r, command=updata)
radio2.pack()
radio3 = tkinter.Radiobutton(win, text="tre", value=66, variable=r, command=updata)
radio3.pack()


win.mainloop()