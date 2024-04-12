from matplotlib import axes, projections
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Gaphics3D:
    @staticmethod
    def showgraph(name_graph, x, y, z, x_name= "", y_name="", z_name=""):
        fig = plt.figure()
        ax = fig.add_subplot(111, projections="3d") 
        # la ligne du dessus ne fonctionne pas

        x_np = np.array(x)
        y_np = np.array(y)
        z_np = np.array(z)

        ax.bar3d(x_np, y_np, np.zeros_like(x_np), 0.5, 0.5, z_np, zsort='average')

        ax.set_title(name_graph)
        ax.set_xlabel(x_name)
        ax.set_ylabel(y_name)
        ax.set_zlabel(z_name)

        plt.show()

    showgraph("3D", 1,2,3,"a", "b", "c")