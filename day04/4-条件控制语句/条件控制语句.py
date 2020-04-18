# -*- coding: utf-8 -*-





'''
if语句



if-else语句





if-elif-else语句
格式：
if  表达式1:
    语句1
elif 表达式2:
    语句2
elif 表达式3:
    语句3
……
elif 表达式n:
    语句n
else:                    #可有可无
    语句e

逻辑：当程序执行到if-elif-else语句时，首先计算“表达式1”的值，如果“表达式1”的值为真，则执行“语句1”，执行完“语句1”，则跳过整个if-elif-else语句。如果“表达式1”的值为假，计算“表达式2”的值。如果“表达式2”的值为真，则执行“语句2”，执行完“语句2”，则跳过整个if-elif-else语句。如果“表达式2”的值为假，计算“表达式3”的值。如此下去直到某个表达式的值为真才停止，如果没有一个真的表达式，且有else，则执行“语句e”
'''


age = int(input())

'''
if age < 0:
    print("娘胎里")
if age >=0 and age <= 3:
    print("婴儿")
if age >=4 and age <= 6:
    print("儿童")
if age >=7 and age <= 18:
    print("童年")
if age >=19 and age <= 30:
    print("青年")
if age >=31 and age <= 40:
    print("壮年")
if age >=41 and age <= 50:
    print("中年")
if age >=51 and age <= 100:
    print("老年")
if age >=101 and age <= 150:
    print("老寿星")
if age > 150:
    print("老妖怪")
'''

'''
if age < 0:
    print("娘胎里")
elif age >=0 and age <= 3:
    print("婴儿")
elif age >=4 and age <= 6:
    print("儿童")
elif age >=7 and age <= 18:
    print("童年")
elif age >=19 and age <= 30:
    print("青年")
elif age >=31 and age <= 40:
    print("壮年")
elif age >=41 and age <= 50:
    print("中年")
elif age >=51 and age <= 100:
    print("老年")
elif age >=101 and age <= 150:
    print("老寿星")
else:
    print("老妖怪")
'''


if age < 0:
    print("娘胎里")
elif age <= 3:
    print("婴儿")
elif age <= 6:
    print("儿童")
elif age <= 18:
    print("童年")
elif age <= 30:
    print("青年")
elif age <= 40:
    print("壮年")
elif age <= 50:
    print("中年")
elif age <= 100:
    print("老年")
elif age <= 150:
    print("老寿星")
else:
    print("老妖怪")

#elif        else if
#每个el都是对它上面所有表达式的否定





'''
女神说：
1、sucnk is a good man
  very good
2、sunck is a nice man
 very nice
3、sunck is a handsome man
 very handsome
4、你是好人
 我们真不合适
5、我希望我们之间存在纯洁友谊
 我们直接也就只能有友谊了
6、你好坏啊
 我感觉我们很合适
'''





