


def outer(func):
    def inner(*args, **kwargs):
        #添加修改的功能
        print("&&&&&&&&&&&&&")
        return func(*args, **kwargs)
    return inner



@outer #say = outer(say)
def say(name, age): #函数的参数力理论上是无限制的，但实际上最好不要超过6、7个
    print("my name is %s, I am %d years old" % (name, age))
    return "aaaa"


say("sunck", 18)





