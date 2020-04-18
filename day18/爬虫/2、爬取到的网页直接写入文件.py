
import urllib.request

urllib.request.urlretrieve("http://www.baidu.com", filename=r"C:\Users\xlg\Desktop\Python-1704\day18\file\file2.html")

#urlretrieve在执行的过程当中，会禅城一些缓存
#清除缓存
urllib.request.urlcleanup()

