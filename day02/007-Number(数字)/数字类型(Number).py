#导入库
#库：封装一些功能
#math：数学相关的库
import math
import random

'''
分类：整数、浮点数、复数
'''

'''
   整数：Python可以处理任意大小的整数，当然包括负整数，在程序中的表示和数学的写法一样
'''
num1 = 10
num2 = num1
print(id(num2))
# 连续定义多个变量
num3 = num4 = num5 = 1
print(num3, num4, num5)
#交互式赋值定义变量
num6, num7 = 6, 7
print(num6, num7)


'''
浮点数：浮点型由整数部分与小数部分组成，浮点数运算可能会有四舍五入的误差
'''
f1 = 1.1
f2 = 2.2
f3 = f1 + f2
print(f3)


'''
复数：实数部分和虚数部分构成
'''


'''
数字类型转换
'''
print(int(1.9))



print(float(1))
print(int("123"))
print(float("12.3"))
#如果有其他无用字符会报错
#print(int("abc"))
#print(int("123abc"))
#只有作为正负号才有意义
print(int("+123"))
#print(int("12+3"))
print(int("-123"))
#print(int("12-3"))


#数学功能

#返回数字的绝对值
a1 = -10
a2 = abs(a1)
print(a2)

#比较两个数的大小
a3 = 100
a4 = 9
print((a3>a4)-(a3<a4))

#返回给定参数的最大值
print(max(1,2,3,4,5,6,7,8))
#返回给定参数的最小值
print(min(1,2,3,4,5,6,7,8))

#求x的y次方  2^5
print(pow(2, 5))

#round(x[,n])返回浮点数x的四舍五入的值，如果给出n值，则代表舍入到小数点后n位
print(round(3.456))
print(round(3.556))
print(round(3.456, 2))
print(round(3.546, 1))


#向上取整
print(math.ceil(18.1))
print(math.ceil(18.9))


#向下取整
print(math.floor(18.1))
print(math.floor(18.9))

#返回整数部分与小数部分
print(math.modf(22.3))

#开方
print(math.sqrt(16))


#随机数

#1从序列的元素中随机挑选一个元素
print(random.choice([1,3,5,7,9]))
print(random.choice(range(5)))#range(5) == [0,1,2,3,4]
print(random.choice("sunck"))#"sunck"  == ["s","u","n","c","k"]

#产生一个1~100之间的随机数
r1 = random.choice(range(10)) + 1
print(r1)


#从指定范围内，按指定的基数递增的集合中选取一个随机数
#random.randrange([start,] stop[, step])
#start--指定范围的开始值，包含在范围内，默认是0
#stop--指定范围的结束之，不包含在范围内
#step--指定的递增基数，默认是1
print(random.randrange(1, 100, 2))
#从0-99选取一个随机数
print(random.randrange(100))

#随机生产[0,1)之间的数(浮点数)
print(random.random())


list = [1,2,3,4,5]
#将序列的所有元素随机排序
random.shuffle(list)
print(list)


#随机生产一个实数，他在[3,9]范围
print(random.uniform(3,9))




#三角函数










