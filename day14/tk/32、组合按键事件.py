import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+200+20")



#<Control-Alt-a>
#<Shift-Up>
#<Control-p>
def func(event):
    print("event.char =", event.char)
    print("event.keycode =", event.keycode)
win.bind("<Control-p>", func)

win.mainloop()