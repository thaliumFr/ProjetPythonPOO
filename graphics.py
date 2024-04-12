import matplotlib.pyplot as plt
import numpy as np

#create class columns graph
class Graphics:
    @staticmethod
    # create columns graph
    def showBar(name_graph, x, y, x_name="", y_name=""):
        x_np = np.array(x)
        y_np = np.array(y)

        plt.bar(x_np, y_np)
        plt.title(name_graph)
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.show()

Graphics.showBar("nom du graph", ["A", "B"], [1, 5], "x")

# create pie charts
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()

#create 2 sets of scatter plots for comparison
#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()