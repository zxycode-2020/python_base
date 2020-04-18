'''什么是字符串
字符串是以单引号或双引号括起来的任意文本
'abc'
"def"
字符串不可变
'''




#创建字符串
str1 = "sunck is a good man!"
str3 = "sunck is a nice man!"
str5 = "sunck is a handsome man!"




'''
字符串运算
'''
#字符串连接
str6 = "sunck is a "
str7 = "good man"
str8 = str6 + str7
print("str6 =", str6)
print("str7 =", str7)
print("str8 =", str8)
#输出重复字符串
str9 = "good"
str10 = str9 * 3
print("str10 =", str10)
#访问字符串中的某一个字符
#通过索引下标查找字符，索引从0开始
#字符串名[下标]
str11 = "sunck is a good man!凯"
print(str11[1])
#str11[1] = "a" #字符串不可变
print("str11 =", str11)

#截取字符串中的一部分
str13 = "sunck is a good man!"
#从给定下标出开始截取到给定下标之前
str15 = str13[6:15]
#从头截取到给定下标之前
str16 = str13[:5]
#从给定下标处开始截取到结尾
str17 = str13[16:]
print("str17 =", str17)


str18 = "sunck is a good man"
print("good" in str18)
print("good1" not in str18)


#print(~5)  #6
'''
00000101
11111010
10000110
'''


#格式化输出
print("sunc is a good man")
num = 10
str19 = "sunck is a nice man!"
f = 10.1267
print("num =", num, "str19 =", str19)
#  %d   %s   %f  占位符
#                                   精确到小数点后3位，会四舍五入
print("num = %d, str19 = %s, f = %.3f" % (num, str19, f))


'''
转义字符   \
将一些字符转换成有特殊含义的字符
'''
#\n
print("num = %d\nstr19 = %s\nf = %.3f" % (num, str19, f))
'''
\\
'''
print("sunck \\ is")

# \'   \"
print('tom is a \'good\' man')
print("tom is a \"good\" man")
#      tom is a 'good' man

#如果字符串内有很多换行，用\n写在一行不好阅读
print("good\nnice\nhandsome")
print('''
good
nice
handsome
''')

'''
\t   制表符
'''
print("sunck\tgood")


#如果字符中有好多字符串都需要转义，就需要加入好多\，为了简化，Python允许用r表示内部的字符串默认不转义
#     \\\t\\
print(r"\\\t\\")
print(r"C:\Users\xlg\Desktop\Python-1704\day03")
print("C:\\Users\\xlg\\Desktop\\Python-1704\\day03")
'''
windows
  C:\\Users\\xlg\\Desktop\\Python-1704\\day03
linux
  /root/user/sunck/Desktop/Python-1704/day03
'''







#eval(str)
#功能：将字符串str当成有效的表达式来求值并返回计算结果
num1 = eval("123")
print(num1)
print(type(num1))
print(eval("+123"))
print(eval("-123"))
print(eval("12+3"))
print(eval("12-3"))
#print(eval("a123"))
#print(eval("12a3"))


#len(str)
#返回字符串的长度(字符个数)
print(len("sunck is a good man凯"))

#lower()转换字符串中大写字母为小写字母
str20 = "SUNCK is a Good Man!凯"
str21 = str20.lower()
print(str21)
print("str20 = %s" %(str20))

#upper()转换字符串中小写字母为大写字母
str21 = "SUNCK is a Good Man!"
print(str21.upper())


#swapcase()转换字符串中小写字母为大写字母,大写字母为小写字母
str22 = "SUNCK is a gOOd mAn!"
print(str22.swapcase())


#capitalize()  首字母大写，其他小写
str23 = "SUNCK is a gOOd mAn!"
print(str23.capitalize())


#title()每个单的首字母大写
str24 = "SUNCK is a gOOd mAn!"
print(str24.title())

#  character   char
#center(width[, fillchar])
#返回一个指定宽度的居中字符串，fillchar为填充的字符串,默认空格填充
str25 = "kaige is a nice man"
print(str25.center(40,"*"))


#ljust(width[, fillchar])
#返回一个指定宽度的左对齐字符串，fllchar为填充字符，默认空格填充
str26 = "kaige is a nice man"
print(str26.ljust(40, "%"))



#rjust(width[, fillchar])
#返回一个指定宽度的右对齐字符串，fllchar为填充字符，默认空格填充
str27 = "kaige is a nice man"
print(str26.rjust(40, "%"))


#zfill(width)
#返回一个长度为width的字符串，原字符串右对齐，前面补0
str28 = "kaige is a nice man"
print(str28.zfill(40))


#count(str[,start][,end])
#返回字符串中strc出现的次数，可以指定一个范围，默认从头到尾
str29 = "kaige is a very very nice man"
print(str29.count("very",15, len(str29) ))



#find(str[, start][,end])
#从左向右检测str字符串是否包含在字符串中，可以指定范围，默认从头到尾。得到的是第一次出现的开始下标，没有返回-1
str30 = "kaige is a very very nice man"
print(str30.find("very"))
print(str30.find("good"))
print(str30.find("very", 15, len(str30)))


#rfind(str[, start][,end])]
str30 = "kaige is a very very nice man"
print(str30.rfind("very"))
#print(str30.rfind("good"))
print(str30.rfind("very", 0, 15))

#index(str, start=0, end=len(str))
#根find()一样，只不过如果str不存在的时候回报一个异常
str31 = "kaige is a very very nice man"
#print(str31.index("good"))


#rindex(str, start=0, end=len(str))
#根rfind()一样，只不过如果str不存在的时候回报一个异常
str32 = "kaige is a very very nice man"
print(str32.rindex("very"))


#lstrip()截掉字符串左侧指定的字符，默认为空格
str33 = "*******kaige is a nice man"
print(str33.lstrip("*"))

#rstrip()截掉字符串右侧指定的字符，默认为空格
str34 = "kaige is a nice man          "
print(str34.rstrip(), "*")


str35 = "*******kaige is a nice man*********"
print(str35.strip("*"))



str36 = "a"
print(ord(str36))
str37 = chr(65)
print(str37)

print(" " != " ")



#split(str="", num)
#以str为分隔符截取字符串,指定num，则仅截取num个字符串
str38 = "sunck**is******a***good*man"
list39 = str38.split("*")
print(list39)
c = 0
for s in list39:
    if len(s) > 0:
        c += 1
print(c)



#splitlines([keepends])   安装('\r', '\r\n',  '\n')分隔
#keepends == True  会保留换行符
str40 = '''sunck is a good man!
sunck is a nice man!
sunck is handsome man!
'''
print(str40.splitlines())



#join(seq)  以指定的字符串分隔符，将seq中的所有元素组合成一个字符串
list41 = ['sunck', 'is', 'a', 'good', 'man']
str42 = "&^%$#".join(list41)
print(str42)


#max()  min()
str43 = "sunck is a good man!z"
print(max(str43))
print("*"+min(str43)+"*")



#replace(oldstr, newstr, count)
#用newstr替换oldstr，默认是全部替换。如果指定了count，那么只替换前count个
str44 = "sunck is a good good good man"
str45 = str44.replace("good", "nice", 1)
print(str44)
print(str45)


#创建一个字符串映射表
print("************")
#                  要转换的字符串     目标字符串
t46 = str.maketrans("ac", "65")
#  a--6    c--5
str47 = "sunck is a good man"
str48 = str47.translate(t46)
print(str48)


#startswith(str, start=0, end=len(str)
#在给定的范围内判断是否是以给定的字符串开头，如果没有指定范围，默认整个字符串
str49 = "sunck is a good  man"
print(str49.startswith("sunck", 5, 16))

#endswith(str, start=0, end=len(str)
#在给定的范围内判断是否是以给定的字符串结尾，如果没有指定范围，默认整个字符串
str50 = "sunck is a nice man"
print(str50.endswith("man"))


#编码
#encode(encoding="utf-8", errors="strict")
str51 = "sunck is a good man凯"
#ignore忽略错误
data52 = str51.encode("utf-8", "ignore")
print(data52)
print(type(data52))

#解码  注意：要与编码时的编码格式一致
str53 = data52.decode("gbk", "ignore")
print(str53)



#isalpha()
#如果字符串中至少有一个字符且所有的字符都是字母返回True,否则返回False
str54 = "sunckisagoodman"
print(str54.isalpha())

#isalnum()
#如果字符串中至少有一个字符且所有的字符都是字母或数字返回True,否则返回False
str55 = "1a2b3"
print(str55.isalnum())


#isupper()
#如果字符串中至少有一个英文字符且所有的英文字符都是大写的英文字母返回True,否则返回False
print("ABC".isupper())
print("1".isupper())
print("ABC1".isupper())
print("ABC#".isupper())


#islower()
#如果字符串中至少有一个英文字符且所有的英文字符都是小写的英文字母返回True,否则返回False
print("abc".islower())
print("abcA".islower())
print("1".islower())
print("abc1".islower())
print("abc#".islower())



#istitle()
#如果字符串是标题化的返回True，否则返回False
print("Sunck Is".istitle())
print("Sunck is".istitle())
print("sunck is".istitle())



#isdigit()
#如果字符串中只包含数字字符返回True，否则范湖False
print("123".isdigit())
print("123a".isdigit())



#isnumeric()同上
print("123".isnumeric())
print("123a".isnumeric())


#字符串中只包含十进制字符
print("123".isdecimal())
print("123z".isdecimal())



#如果字符中只包含空格则返回True,否则返回False
print(" ".isspace())
print("      ".isspace())
print("\t".isspace())
print("\n".isspace())
print("\r".isspace())




















