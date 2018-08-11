#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import os
import codecs

# for test
def createFile(fileName, filePath):
    filePath = filePath + "\\" + fileName
    with open(filePath, 'w', newline='') as f:
        rows = [['1', '2', '3'], ['4', '5', '6']]

        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)
    with open(filePath, 'a+', newline='') as f:
        rows = [['3', '4', '5'], ['4', '5', '6']]
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

    with open(filePath, 'r+', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(str(row))


class FileOp:
    def __init__(self, folderPath, fileName):
        self.folderPath = folderPath
        self.fileName = fileName

        print(fileName)
        self.f = self.__output2File()

    def __del__(self):
        if hasattr(self,"f"):
            print("close !!!!!")
            self.f.close()
            return
        print("f is not exist")

    def __output2File(self):

        filePath = self.folderPath + "\\" + self.fileName
        if os.path.exists(self.folderPath) is False:
            os.makedirs(self.folderPath)
        if not os.path.exists(filePath):
            flag = 'w'
        else:
            os.remove(filePath)
            flag = 'a'
        return open(filePath, flag, newline='')

    def addRow(self, rowContent):
        writer = csv.writer(self.f)
        writer.writerow(rowContent)

    @staticmethod
    def showContent(folderPath, fileName):
        filePath = folderPath + "\\" + fileName
        rows = []
        with open(filePath, 'r+', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                rows.append(row)
                # print(str(row))
        return rows

    @staticmethod
    def readSql(folderPath, fileName):
        filePath = folderPath + "\\" + fileName
        with open(filePath, 'r+', encoding='utf-8') as f:
            # firstLine = f.read()
            # if firstLine[:3] == codecs.BOM_UTF8:
            #     print("dddd")
            return "".join(f.readlines())


# if __name__ == '__main__':
#     # createFile("Test.csv", "e:\\hhh")
#     # print(FileOp.output2File("e:\\hhh2", "Test.csv"))
#     f = FileOp("e:\\hhh2", "Test.csv")
#     f.addRow([1, 2, 3, 4, 5])
#     f.showContent()
