from dealFile import DealFile

d = DealFile()

toPath = r"C:\Users\xlg\Desktop\Python-1704\day16\0-作业\读写csv\csv\sunck.csv"

for i in range(2, 5):
    path = r"C:\Users\xlg\Desktop\Python-1704\day16\0-作业\读写csv\csv\00000" + str(i) + ".csv"
    listInfo = d.readCsv(path)
    d.writeCsv(toPath, listInfo)

allInfo = d.readCsv(toPath)



