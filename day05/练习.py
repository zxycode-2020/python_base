
w = input()
d = {}  #  word:次数

str = "sunck is a good man! sunck is a nice man! sunck is a hands man! sunck is a good man! sunck is a nice man! sunck is a great man! sunck is a noble man! sunck is a cool man!"


l = str.split(" ")
for v in l:
    c = d.get(v)
    if c == None:
        d[v] = 1
    else:
        d[v] += 1

print(d[w])

'''
1、以空格切割字符串
2、循环处理列表中的每个元素
3、以元素当做key去一个字典中提取数据
4、如果没有提取到，就以该元素作为key，1作为value 存进字典
5、如果提取到，将对应的key的value修改，值加1
6、根据输入的字符串当做key再去字典取值
'''











