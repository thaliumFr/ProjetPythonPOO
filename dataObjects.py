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

print(dataImportOC.header)

Graphics.showBar("Note moyenne par jeux", labels, values, "Noms des jeux", "Notes")