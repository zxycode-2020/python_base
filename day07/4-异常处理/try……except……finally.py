'''
try……except……finally
格式：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
……
except 错误码 as e:
    语句n
finally:
    语句f

作用：语句t无论是否有错误都讲执行最后的语句f

'''

try:
    print(1/1)
except NameError as e:
    print("为0了")
finally:
    print("必须执行我")






