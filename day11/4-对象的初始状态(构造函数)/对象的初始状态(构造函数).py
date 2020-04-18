
class Person(object):
    #name = "stu"
    #age = 10
    #height = 160
    #weight = 90
    def run(self):
        print("run")
    def eat(self, food):
        print("eat " + food)

    def __init__(self, name, age, height, weight):
        #print(name, age, height, weight)
        #定义属性
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

'''
构造函数：__init__()   在使用类创建对象的时候自动调用
注意：如果不显示的写出构造函数，默认会自动添加一个空的构造函数
'''
per = Person("hanmeimei", 20, 170, 55)
print(per.name, per.age)

per2 = Person("lilei", 21, 175, 70)
print(per2.name, per2.age)

per.run()


