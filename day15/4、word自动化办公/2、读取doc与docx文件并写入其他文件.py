import win32com
import win32com.client

def readWordFileToOtherFile(path, toPath):
    mw = win32com.client.Dispatch("Word.Application")
    doc = mw.Documents.Open(path)

    #将word的数据保存到另一个文件
    doc.SaveAs(toPath, 2)#2表示为txt文件

    doc.Close()
    mw.Quit()

path = r"C:\Users\xlg\Desktop\Python-1704\day15\4、word自动化办公\sunck.doc"
toPath = r"C:\Users\xlg\Desktop\Python-1704\day15\4、word自动化办公\a.txt"
readWordFileToOtherFile(path, toPath)





