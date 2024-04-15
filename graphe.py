import matplotlib.pyplot as plt
import numpy as np
import csv
from SaveSystem import Csv
from dataImporter import DataImporter


class Graphics3D:
    
    @staticmethod
    def historigram3D():
        data = Csv.Load("OpenCritics")
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        dataImportOC = Csv.Load("OpenCritics")

        devs = dataImportOC.GetColumn(2)
        release = dataImportOC.GetColumn(3)
       
        

        hist, xedges, yedges = np.histogram2d(devs, release, bins=10, range=[[min(devs), max(devs)], [min(release), max(release)]])

            # Construct arrays for the anchor positions of the 16 bars.
        xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
        xpos = xpos.ravel()
        ypos = ypos.ravel()
        zpos = 0

            # Construct arrays with the dimensions for the 16 bars.
        dx = dy = 0.5 * np.ones_like(zpos)
        dz = hist.ravel()

        ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')

        ax.set_xlabel('Studio')
        ax.set_ylabel('Année')
        ax.set_zlabel('Prix')

        
        ax.set_xticks(devs)
        ax.set_xticklabels([data.content[i][2] for i in range(2)], rotation=75)


    @staticmethod
    def scatterplot():
        np.random.seed(19680801)


        def randrange(n, vmin, vmax):
            return (vmax - vmin)*np.random.rand(n) + vmin

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        n = 100

        # For each set of style and range settings, plot n random points in the box
        # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
        for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
            xs = randrange(n, 1, 12)
            ys = randrange(n, 2014, 2024)
            zs = randrange(n, zlow, zhigh)
            ax.scatter(xs, ys, zs, marker=m)

        ax.set_xlabel('Mois')
        ax.set_ylabel('Année')
        ax.set_zlabel('Quantité')
 

# Appel de la méthode historigram3D de manière statique
Graphics3D.historigram3D()

# Appel de la méthode scatterplot de manière statique
Graphics3D.scatterplot()

plt.show()