import csv

import win32com
import win32com.client

import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


class DealFile(object):
    #读取csv
    def readCsv(self, path):
        infoList = []
        with open(path, "r") as f:
            allFileInfo = csv.reader(f)
            for row in allFileInfo:
                infoList.append(row)
        return infoList
    #写csv
    # [["1","2","3"],["4","5","6"],["7","8","9"]]
    def writeCsv(self, path, data):
        with open(path, "w") as f:
            writer = csv.writer(f)
            for rowData in data:
                #print("rowData = ", rowData)
                writer.writerow(rowData)
    #pdf
    def readPDF(self, path, callback=None,toPath=""):
        f = open(path, "rb")
        parser = PDFParser(f)
        pdfFile = PDFDocument()
        parser.set_document(pdfFile)
        pdfFile.set_parser(parser)
        pdfFile.initialize()
        if not pdfFile.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            manager = PDFResourceManager()
            laparams = LAParams()
            device = PDFPageAggregator(manager, laparams=laparams)
            interpreter = PDFPageInterpreter(manager, device)
            for page in pdfFile.get_pages():
                interpreter.process_page(page)
                layout = device.get_result()
                for x in layout:
                    if (isinstance(x, LTTextBoxHorizontal)):
                        if toPath == "":
                            # 处理每行数据
                            str = x.get_text()
                            if callback != None:
                                callback(str)
                            else:
                                print(str)
                        else:
                            #写文件
                            print("将PDF数据写入文件")

    def readWordFile(path):
        mw = win32com.client.Dispatch("Word.Application")
        doc = mw.Documents.Open(path)
        for paragraph in doc.Paragraphs:
            line = paragraph.Range.Text
            print(line)
        doc.Close()
        mw.Quit()




