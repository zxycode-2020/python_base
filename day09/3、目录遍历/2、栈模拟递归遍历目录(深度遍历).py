import os

def getAllDirDE(path):
    stack = []
    stack.append(path)

    #处理栈，当栈为空的时候结束循环
    while len(stack) != 0:
        #从栈里取出数据
        #[]
        dirPath = stack.pop()
        #print(dirPath)
        #目录下所有文件
        filesList = os.listdir(dirPath)
        #print(filesList)
        #处理每一个问价，如果是普通文件则打印出来，如果是目录则将该目录的地址压栈
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                #是目录就压栈
                print("目录：" + fileName)
                stack.append(fileAbsPath)
                #["B", "E", "F"]
            else:
                #打印普通文件
                print("普通：" + fileName)



getAllDirDE(r"C:\Users\xlg\Desktop\Python-1704\day09\temp\dir")









