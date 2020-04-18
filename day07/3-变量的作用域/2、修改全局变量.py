
num = 10
print(id(num))
def func():
    #声明num为全局变量，方便在函数中修改
    global num
    # 修改num
    num = 20
    print(id(num))
    #可以使用，但是无法直接修改
    #num = 20#相当于在函数内部定义了一个num
    #print(id(num))
    #可以直接使用外部全局变量的的值
    print("num =", num)

func()
print("外部打印num =", num)
print(id(num))