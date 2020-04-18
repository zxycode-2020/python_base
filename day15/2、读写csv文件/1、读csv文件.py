import csv

def readCsv(path):
    infoList = []
    with open(path, "r") as f:
        allFileInfo = csv.reader(f)
        for row in allFileInfo:
            infoList.append(row)
    return infoList

path = r"C:\Users\xlg\Desktop\Python-1704\day15\2、读写csv文件\000001.csv"
info = readCsv(path)

