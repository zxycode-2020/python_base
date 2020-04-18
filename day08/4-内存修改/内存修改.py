#进程模块
import  win32process
import win32con
import win32gui
import win32api
import ctypes
import time


PROCESS_ALL_ACCESS = (0x000F0000|0x00100000|0xFFF)
ID = 0x115d9ac8
#找窗体
win = win32gui.FindWindow("MainWindow", "植物大战僵尸中文版")
#根据窗体找到进程号
hid, pid = win32process.GetWindowThreadProcessId(win)
print(pid)
#以最高权限打开进程
p = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
#加载内核模块
md = ctypes.windll.LoadLibrary("C:\\Windows\\System32\\kernel32")
data = ctypes.c_long()
#读取内存
md.ReadProcessMemory(int(p), ID, ctypes.byref(data), 4, None)
print("data =", data)
while 1:
    time.sleep(5)
    #新值
    newData = ctypes.c_long(10000)
    #修改
    md.WriteProcessMemory(int(p), ID, ctypes.byref(newData), 4, None)

















