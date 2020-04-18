#1
'''
num = 100
while num  <= 999:
    a = num % 10
    b = num // 10 % 10
    c = num // 100

    if num == a**3 + b**3 + c**3:
        print(num)
    num += 1


'''


'''
num = int(input())
if num == 2:
    print("是质数")
index = 2
while index <= num - 1:
    if num % index == 0:
        print("不是质数")
    index += 1

if index == num:
    print("是质数")
'''
'''
str = input()
index = 0
sum = 0
while index < len(str):
    if str[index] >= "0" and str[index] <= "9":
        sum += int(str[index])
    index += 1

print("sum = %d" %(sum))
'''
#字符串比较大小
#从第一个字符开始比较,谁的ASCII值大谁就大,如果相等会比较下一个字符的ASCII值大小，那么谁的值大谁就大
print("ms" == "ms")#  \0

