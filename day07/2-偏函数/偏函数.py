import functools

#
print(int("1010", base = 2))

#偏函数
def int2(str, base = 2):
    return int(str, base)
print(int2("1011"))


#把一个参数固定住，形成一个新的函数
int3 = functools.partial(int, base = 2)
print(int3("111"))





