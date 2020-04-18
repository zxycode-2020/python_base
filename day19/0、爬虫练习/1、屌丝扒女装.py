import urllib.request
import re
import os

def imageCrawler(url, toPath):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    HtmlStr = response.read().decode("utf-8")
    #with open(r"C:\Users\xlg\Desktop\Python-1704\day19\0、爬虫练习\yhd.html", "wb") as f:
    #    f.write(HtmlStr)

    pat = r'<img style="width:230px;height:322px" src="//(.*?)"/>'
    re_image = re.compile(pat, re.S)
    imagesList = re_image.findall(HtmlStr)
    num = 1
    for imageUrl in imagesList:
        path = os.path.join(toPath, str(num)+".jpg")
        num += 1
        #把图片下载到本地存储
        urllib.request.urlretrieve("http://"+imageUrl, filename=path)


url = "http://list.yhd.com/c28115-0-90896/?tc=0.0.16.CatMenu_Search_100000040_154700.128&tp=1.1.3433.7.2.LrEpYl6-10-9JhO4&ti=TG6299"
toPath = r"C:\Users\xlg\Desktop\Python-1704\day19\0、爬虫练习\image"
imageCrawler(url, toPath)



