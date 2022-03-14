import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def line_passing (p1, p2, p3):
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(p1,p2,p3)
    ax.scatter(p1,p2,p3, marker="*", c="red")
    
p1 = np.linspace(30,85,3)

p2 = np.linspace(6,60,3)

p3 = np.linspace(80,50,3)

line_passing (p1, p2, p3)

plt.show()
