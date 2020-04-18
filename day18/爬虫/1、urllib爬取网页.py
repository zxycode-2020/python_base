import urllib.request

# 向指定的url地址发起请求，并返回服务器响应的数据(文件的对象)
response = urllib.request.urlopen("http://www.baicu.com")

# 读取问文件的全部内容，会把读取到的数据赋值给一个字符串变量
data = response.read()
print(data)
print(type(data))

# 读取一行
#data = response.readline()

#读取文件的全部内容，会把读取到的数据赋值给一个列表变量
#data = response.readlines()
'''
print(data)
print(type(data))
print(len(data))
print(type(data[100].decode("utf-8")))
'''



#将爬取到的网页写入文件
# with open(r"C:\Users\xlg\Desktop\Python-1704\day18\file\file1.html", "wb") as f:
#     f.write(data)


#response 属性
#返回当前环境的有关信息
print(response.info())

#返回状态码
print(response.getcode())
#if response.getcode() == 200 or response.getcode() == 304:
    #处理网页信息
#    pass

#返回当前正在爬取的URL地址
print(response.geturl())


#
'''
url = r"https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E5%87%AF%E5%93%A5%E5%AD%A6%E5%A0%82&rsv_pq=96b2af980000cb00&rsv_t=ed0aZ%2FMEmvroTfrwq5E%2FJFwohlrfGzQfpCwXWirqpFgzTvJwE9WdPgDp4Jk&rqlang=cn&rsv_enter=1&rsv_sug3=3&rsv_sug1=2&rsv_sug7=100&rsv_sug2=1&prefixsug=%25E5%2587%25AF%25E5%2593%25A5&rsp=0&inputT=4668&rsv_sug4=5958"
#解码
newUrl = urllib.request.unquote(url)
print(newUrl)
#编码
newUrl2 = urllib.request.quote(newUrl)
print(newUrl2)
'''

