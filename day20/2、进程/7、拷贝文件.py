import os, time
from multiprocessing import Pool



#实现文件的拷贝
def copyFile(rPath, wPath):
    fr = open(rPath, "rb")
    fw = open(wPath, "wb")
    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()


path = r"C:\Users\xlg\Desktop\Python-1704\day20\2、进程\file"
toPath = r"C:\Users\xlg\Desktop\Python-1704\day20\2、进程\toFile"


#读取path下的都有的文件
filesList = os.listdir(path)

#启动for循环处理每一个文件
start = time.time()
for fileName in filesList:
    copyFile(os.path.join(path,fileName), os.path.join(toPath,fileName))
end = time.time()
print("总耗时：%0.2f" % (end-start))