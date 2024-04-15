import matplotlib.pyplot as plt
import numpy as np
import csv
from SaveSystem import Csv
fileCSV = Csv.Load("OpenCritics")

class DataImporter:
    def __init__(self, csvFile):
        self.rows = []
        with open(csvFile, 'r') as file:
            csvreader = csv.reader(file, delimiter = ";")
            self.header = next(csvreader)
            for row in csvreader:
                self.rows.append(row)

    def getColumnData(self, columnName):
        data = []
        for row in self.rows:
            colIdx = self.header.index(columnName)
            data.append(row[colIdx])
        return data

# rows = []
# with open("OpenCritics.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
# print(header)
# print(rows, sep=",\n")

# labels = []
# values = []

# lists = Csv.Load("OpenCritics").content
# for list in lists:
#     for object in list:
#         print(object)