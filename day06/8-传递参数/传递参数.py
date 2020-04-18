'''
值传递：传递的不可变类型
string、tuple、number是不可变的
'''
def func1(num):
    print(id(num))
    num = 10
    print(id(num))

temp = 20
print(id(temp))
func1(temp)   #num = temp
print(temp)

'''
引用传递：传递的可变类型
list、dict、set是可变的
'''
def func2(lis):
    lis[0] = 100
li = [1,2,3,4,5]
func2(li)
print(li)


a = 10
b = 10
b = 40
print(id(a), id(b))

c = 20
d = 30
print(id(c), id(d))
d = c
print(id(c), id(d))




