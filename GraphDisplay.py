import matplotlib.pyplot as plt
import numpy as np
import csv
# from SaveSystem import Csv

# fileCSV = Csv.Load("OpenCritics")


# create class columns graph
class GraphDisplay:
    def __init__(self, nbOfPlots):
        self.fig, self.ax = plt.subplots(1, nbOfPlots, figsize=(15, 8))
        plt.subplots_adjust(bottom=.3)
        self.pltIdx = 0

    def addBar(self, title: str, x: list, y: list):
        x_np = np.array(x)
        y_np = np.array(y)

        self.ax[self.pltIdx].bar(x_np, y_np)
        self.ax[self.pltIdx].set_title(title)
        for tick in self.ax[self.pltIdx].get_xticklabels():
            tick.set_rotation(-90)
            tick.set_fontsize(8)
        self.pltIdx += 1

    def display(self):
        plt.show()

    # create columns graph
    def showBar(title: str, x: list, y: list, x_name="", y_name=""):
        x_np = np.array(x)
        y_np = np.array(y)

        plt.bar(x_np, y_np)
        plt.title(title)
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.xticks(rotation=60, fontsize=11)
        plt.show()

    # create pie charts
    def showPie(title: str, shares: list, mylabels=[]):
        y_np = np.array(shares)

        plt.pie(y_np, labels=shares)
        plt.legend(mylabels)
        plt.title(title)
        plt.show()

    # create 2 sets of scatter plots for comparison
    def show2setsPlots(title: str, values: list, x_name="", y_name=""):
        for value in values:
            x = []
            y = []
            for point in value:
                x.append(point[0])
                y.append(point[1])
            x_np = np.array(x)
            y_np = np.array(y)
            plt.scatter(x_np, y_np)
        plt.autoscale()
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.show()


if __name__ == "__main__":
    GraphDisplay.showBar("nom du graph", ["A", "B"], [1, 5], "x")
    GraphDisplay.showPie(
        "nom graph", [35, 15, 23, 27], ["chiens", "chats", "poissons", "chevaux"]
    )
    GraphDisplay.show2setsPlots("nom graphe", [[(1, 5), (2, 7)], [(5, 6), (9, 5), (6, 1)]])
