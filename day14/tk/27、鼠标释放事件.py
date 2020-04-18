import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+200+20")

#<ButtonRelease-1>释放鼠标左键
#<ButtonRelease-3>释放鼠标右键
#<ButtonRelease-2>释放鼠标中键
label = tkinter.Label(win, text="sunck is a good man", bg="red")
label.pack()
def func(event):
    print(event.x, event.y)
label.bind("<ButtonRelease-1>", func)




win.mainloop()