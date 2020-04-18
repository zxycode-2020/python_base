

import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+200+20")

label = tkinter.Label(win, text="sunck is a good man", bg="red")
#设置焦点
label.focus_set()
label.pack()


#<Shift_L>  左shift
#<Shift_R>
#<F5>
#<Return>   回车
#<BackSpace>   退格
def func(event):
    print("event.char =", event.char)
    print("event.keycode =", event.keycode)
label.bind("<Shift_L>", func)

win.mainloop()







