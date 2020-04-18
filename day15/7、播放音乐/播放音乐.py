import time
import pygame
#pip  install  pygame
#http://www.3366.com/flash/97506.shtml
#音乐路径
filePath = r"C:\Users\xlg\Desktop\Python-1704\day15\7、播放音乐\res\0.mp3"

#初始化
pygame.mixer.init()
#加载音乐
track = pygame.mixer.music.load(filePath)
#播放
pygame.mixer.music.play()
#
time.sleep(5)
#停止
pygame.mixer.music.stop()




