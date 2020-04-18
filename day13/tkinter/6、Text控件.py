import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("sunck")
#设置大小和位置
win.geometry("400x400+200+20")


'''
文本控件，用于显示多行文本
'''

#height显示的行数
text = tkinter.Text(win, width=30, height=4)
text.pack()
str = '''If there is anyone out there who still doubts that America is a place where all things are possible, who still wonders if the dream of our founders is alive in our time, who still questions the power of our democracy, tonight is your answer'''
text.insert(tkinter.INSERT, str)


win.mainloop()

















