from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot
v = np.array([2.0, 2.0, 4.0])

e0 = np.array([1., 0., 0.])
e1 = np.array([0., 1., 0.])
e2 = np.array([0., 0., 1.])

project_e0 = np.dot(e0, v[0])
project_e1 = np.dot(e1, v[1])
project_e2 = np.dot(e2, v[2])

ax = matplotlib.pyplot.axes(projection = "3d")

ax.plot3D(project_e0, project_e1, project_e2, "blue")
matplotlib.pyplot.show()