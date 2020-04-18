import tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+200+0")


'''
列表框控件，可以包含一个或者多个文本框
作用：在listbox控件的小窗口显示一个字符串

'''

#1、创建一个listbox, 添加几个元素
lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE)
lb.pack()
for item in ["good", "nice", "handsome", "vg", "vn"]:
    #按顺序添加
    lb.insert(tkinter.END, item)
#在开始添加
lb.insert(tkinter.ACTIVE, "cool")
#将列表当成一个元素添加的
#lb.insert(tkinter.END, ["very good", "very nice"])
#删除  参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只删除第一个索引处的内容
#lb.delete(1,3)
#lb.delete(1)
#选中   参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只选中第一个索引处的内容
lb.select_set(2,5)
#lb.select_set(2)
#取消
#lb.select_clear(2,4)
#lb.select_clear(3)
#获取到列表中的元素的个数
#print(lb.size())
#从列表中取值  参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只获取第一个索引处的内容
#print(lb.get(2, 4))
#print(lb.get(2))

#返回当前的索引项，不是item元素
print(lb.curselection())
#判断  一个选项是否被选中
print(lb.selection_includes(1))
print(lb.selection_includes(3))



win.mainloop()