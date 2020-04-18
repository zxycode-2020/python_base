import os
import collections

def getAllDirQU(path):
    queue = collections.deque()
    #进队
    queue.append(path)
    while len(queue) != 0:
        #出队数据
        dirPath = queue.popleft()
        #找出所有的文件
        filesList = os.listdir(dirPath)

        for fileName in filesList:
            #绝对路径
            fileAbsPath = os.path.join(dirPath, fileName)
            #判断是否是目录，是目录就进队，不是就打印
            if os.path.isdir(fileAbsPath):
                print("目录：" + fileName)
                queue.append(fileAbsPath)
            else:
                print("普通文件：" + fileName)


getAllDirQU(r"C:\Users\xlg\Desktop\Python-1704\day09\temp\dir")











