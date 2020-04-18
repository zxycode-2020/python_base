import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+200+20")

#<Enter>鼠标光标进入控件时触发
#<Leave>鼠标光标离开控件时触发
label = tkinter.Label(win, text="sunck is a good man", bg="red")
label.pack()
def func(event):
    print(event.x, event.y)
label.bind("<Leave>", func)




win.mainloop()