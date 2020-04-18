import win32com
import win32com.client

def makePPT(path):
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True

    #增加一个文件
    pptFile = ppt.Presentations.Add()

    #创建页  参数1为页数(从1开始)  参数2为类型
    page1 = pptFile.Slides.Add(1,1)
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = "sunck"
    t2 = page1.Shapes[1].TextFrame.TextRange
    t2.Text = "sunck is a good man"

    page2 = pptFile.Slides.Add(2, 1)
    t3 = page2.Shapes[0].TextFrame.TextRange
    t3.Text = "kaige"
    t4 = page2.Shapes[1].TextFrame.TextRange
    t4.Text = "kaige is a good man"

    page2 = pptFile.Slides.Add(3, 2)

    #保存
    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()



path = r"C:\Users\xlg\Desktop\Python-1704\day15\6、ppt自动化办公\sunck.ppt"
makePPT(path)


