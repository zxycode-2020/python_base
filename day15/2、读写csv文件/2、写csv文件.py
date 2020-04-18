import csv

def writeCsv(path, data):
    with open(path, "w") as f:
        writer = csv.writer(f)
        for rowData in data:
            print("rowData = ", rowData)
            writer.writerow(rowData)


path = r"C:\Users\xlg\Desktop\Python-1704\day15\2、读写csv文件\000002.csv"
writeCsv(path, [["1","2","3"],["4","5","6"],["7","8","9"]])
