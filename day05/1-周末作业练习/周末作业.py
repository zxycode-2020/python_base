import random
import turtle
'''
1 x 1 = 1
2 x 1 = 2  2 x 2 = 4
3 x 1 = 3  3 x 2 = 6  3 x 3 = 9
……
9 x 1 = 9  9 x 2 = 18
'''
'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d x %d = %d" % (i, j, i * j), end=" ")
    print("")
'''


'''
#10 20
num1 = int(input())
num2 = int(input())

index = 1
max = 0
while index <= num1:
    if num1 % index == 0 and num2 % index == 0:
        max = index
    index += 1

print(max)
'''

'''
str = input()
res = ""
for i in str:
    if i >= 'a' and i <= 'z':
        ch = chr(ord(i) - 32)
        res += ch
    elif i >= 'A' and i <= 'Z':
        ch = chr(ord(i) + 32)
        res += ch
    else:
        res += i
print(res)
'''




'''
str = ""
for i in range(6):
    ty = random.randrange(3)
    if ty == 0:
        #随机生成一个大写字母
        ch = chr(random.randrange(ord('A'), ord('Z') + 1))
        str += ch
    elif ty == 1:
        # 随机生成一个小写字母
        ch = chr(random.randrange(ord('a'), ord('z') + 1))
        str += ch
    else:
        # 随机生成一个数字
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str += ch
print(str)
'''






# 0,0   100,0     100,100   0,100

'''
turtle.forward(100)
turtle.goto(100, 100)
turtle.goto(0, 100)
turtle.goto(0, 0)
'''
'''
turtle.up()
turtle.goto(50, 50)
turtle.down()
turtle.goto(50, -50)
turtle.goto(-50, -50)
turtle.goto(-50, 50)
turtle.goto(50, 50)
'''

'''
turtle.goto(100, 0)
turtle.goto(100, 100)
turtle.goto(0, 100)
turtle.goto(0, 0)

turtle.goto(50, 50)
turtle.goto(150, 50)
turtle.goto(150, 150)
turtle.goto(50, 150)
turtle.goto(50, 50)

turtle.up()
turtle.goto(0, 100)
turtle.down()
turtle.goto(50, 150)


turtle.up()
turtle.goto(100, 100)
turtle.down()
turtle.goto(150, 150)

turtle.up()
turtle.goto(100, 0)
turtle.down()
turtle.goto(150, 50)
'''
'''
step = 20
turtle.speed(10)
for i in range(19):
    turtle.up()
    turtle.goto(0, step * i)
    turtle.down()

    turtle.goto(360, step * i)
for j in range(19):
    turtle.up()
    turtle.goto(step * j, 0)
    turtle.down()

    turtle.goto(step * j, 360)
'''

step = 20
turtle.speed(10)
for i in range(8):
    for j in range(8):
        turtle.up()
        turtle.goto(step * j, step * i)
        turtle.down()

        turtle.begin_fill()
        for m in range(4):
            turtle.forward(step)
            turtle.left(90)

        if (i + j) % 2 != 0:
            turtle.fillcolor("white")
        else:
            turtle.fillcolor("black")

        turtle.end_fill()

turtle.done()


























