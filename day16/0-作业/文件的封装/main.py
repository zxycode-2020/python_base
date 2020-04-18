from dealFile import DealFile

d = DealFile()

path = r"C:\Users\xlg\Desktop\Python-1704\day16\0-作业\文件的封装\sunck.pdf"

def func(str):
    print(str + "!")

#              回调函数
d.readPDF(path, func)

