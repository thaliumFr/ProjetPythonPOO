import matplotlib.pyplot as plt
import numpy as np
import csv
from dataImporter import DataImporter
from graphics import Graphics
from SaveSystem import Csv
fileCSV = Csv.Load("OpenCritics")



dataImportOC = DataImporter("OpenCritics.csv")
labels = dataImportOC.getColumnData("Name")
values = dataImportOC.getColumnData("note AVG")
idx = 0
while idx < len(labels):
    if values[idx] == "none":
        del values[idx]
        del labels[idx]
        continue
    idx += 1

Graphics.showBar("Note moyenne par jeux", labels, values, "Noms des jeux", "Notes")