import urllib.request
import ssl
import re
import os
from collections import deque

def writeFileBytes(htmlBytes, toPath):
    with open(toPath, "wb") as f:
        f.write(htmlBytes)
def writeFileStr(htmlBytes, toPath):
    with open(toPath, "w") as f:
        f.write(str(htmlBytes))
def getHtmlBytes(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    return response.read()
def qqCrawler(url, toPath):
    htmlBytes = getHtmlBytes(url)
    htmlStr = str(htmlBytes)
    pat = r'(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)'
    re_url = re.compile(pat)
    urlsList = re_url.findall(htmlStr)
    # 去重
    urlsList = list(set(urlsList))
    pat = r"[1-9]\d{4,9}"
    re_qq = re.compile(pat)
    qqsList = re_qq.findall(htmlStr)
    # 去重
    qqsList = list(set(qqsList))
    f = open(toPath,"a")
    for qqStr in  qqsList:
        f.write(qqStr+"\n")
    f.close()
    return urlsList




def center(url, toPath):
    queue = deque()
    queue.append(url)
    while len(queue) != 0:
        targetUrl = queue.popleft()
        urlList = qqCrawler(targetUrl, toPath)
        for item in urlList:
            tempUrl = item[0]
            queue.append(tempUrl)

url = "https://www.douban.com/group/topic/41011762/?start=1100"
toPath = r"C:\Users\xlg\Desktop\Python-1704\day19\0、爬虫练习\爬取网络中的QQ号码\qqFile.txt"
center(url, toPath)













