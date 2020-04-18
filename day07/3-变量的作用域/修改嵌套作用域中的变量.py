'''
def outer():
    num = 10
    def inner():
        #修改num
        nonlocal num
        num = 20
        print("在inner里打印num =", num)
    inner()
    print("在outer里打印num =", num)
outer()
'''

def outer():
    num = 10
    def inner():
        nonlocal num
        num = 20
        def little():
            nonlocal num
            num = 30
            print("在little里打印Num =", num)
        little()
        print("在inner里打印num =", num)
    inner()
    print("在outer里打印num =", num)
outer()