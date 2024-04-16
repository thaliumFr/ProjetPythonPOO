import json
import platform
import matplotlib.pyplot as plt
import numpy as np
import csv
from dataImporter import DataImporter
from GraphDisplay import GraphDisplay
# from SaveSystem import Csv
# fileCSV = Csv.Load("OpenCritics")

dataImportOC = DataImporter("SteamGames.csv")

names = dataImportOC.getColumnData("name")
prices = dataImportOC.getColumnData("price")
devs = dataImportOC.getColumnData("devs") # mixed single quotes and double quotes render this unparseable properly
isMultiplayer = dataImportOC.getColumnData("IsMultiplayer")
platforms = dataImportOC.getColumnData("platforms")

# devs = [json.loads(dev) for dev in devs]
# platforms = [json.loads(plat.replace("'", '"')) for plat in platforms]

for i, plat in enumerate(platforms):
    platforms[i] = json.loads(plat.replace("'", '"').replace("True", "true").replace("False", "false"))

prices = [price[:-1] for price in prices if len(price) > 0]

# Need to parse the prices (format is all over the place)
# Need to use the platforms in a pie chart (combine the dict values)

exit()

gradeFilteredNames = names.copy()
idx = 0
while idx < len(gradeFilteredNames):
    if avgGrades[idx] == "none":
        del avgGrades[idx]
        del gradeFilteredNames[idx]
        continue
    idx += 1

criticsFilteredNames = names.copy()
idx = 0
while idx < len(criticsFilteredNames):
    if criticsGrades[idx] == "none":
        del criticsGrades[idx]
        del criticsFilteredNames[idx]
        continue
    idx += 1
criticsGrades = [val[:-1] for val in criticsGrades]

devGrades = [(dev, grade) for (dev, grade) in zip(devs, avgGrades)]
uDevs = list(set(devs))
avgs = []

idx = 0
while idx < len(uDevs):
    avg = 0
    nbGrades = 0
    for (devName, grade) in devGrades:
        if (devName == uDevs[idx]):
            nbGrades += 1
            avg += int(grade)
    if (nbGrades != 0):
        avg /= nbGrades
        avgs.append(avg)
        idx += 1
    else:
        del uDevs[idx]

# print(list(zip(uDevs, avgs)))

disp = GraphDisplay(3)

proc = lambda s: (s[:32] +  "...") if len(s) > 35 else s
disp.addBar("Note moyenne par jeux", list(map(proc, gradeFilteredNames)), avgGrades)
disp.addBar("Note des critiques", list(map(proc, criticsFilteredNames)), criticsGrades)
disp.addBar("Note moyenne par développeurs", list(map(proc, uDevs)), avgs)

disp.display()

# GraphDisplay.showBar("Note moyenne par jeux", gradeFilteredNames, avgGrades, "Noms des jeux", "Notes")
# GraphDisplay.showBar("Notes des critiques", criticsFilteredNames, criticsGrades, "Noms des jeux", "Notes")