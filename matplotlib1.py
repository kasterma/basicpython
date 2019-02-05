# following along with the Pyplot tutorial at http://matplotlib.org/tutorials/introductory/pyplot.html

import matplotlib.pyplot as plt
import numpy as np

# basic plot with labels
plt.plot([1, 2, 3, 5])
plt.ylabel("Some numbers")
plt.xlabel("input")

# add some text
plt.plot([1, 2, 4], [11, 8, 12], 'ro')
plt.axis([0, 5, 4, 12])
plt.text(2, 6, "hello")
plt.text(1, 5, "hello", fontsize=20)
plt.text(1, 5, "hello", horizontalalignment='center')

# multiple sequences in the same plot (command)
t = np.arange(0, 5, 0.2)
plt.plot(t, t, 'r--', t, np.power(t, 2), 'bs')

# bubble plot
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')

# categorical variables
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(1, figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.subplot(131)    ## deprecated to go back to earlier subplot like this
plt.ylabel("lab lab")

p1 = plt.plot([1, 2, 3], [4, 4, 6])
plt.setp(p1, color='b', linestyle='-.')
plt.setp(p1)

f1 = plt.figure(1)
plt.subplot(211)
plt.plot([1 ,2], [1, 2])

f2 = plt.figure(2)
plt.plot([1, 2], [11, 10])

plt.figure(1)
plt.subplot(2, 1, 2)
plt.plot([1, 2], [33, 32])
plt.subplot(1, 1, 1)
plt.plot([11,22], [33,44])
plt.figure(2)
plt.subplot(3, 1, 2)
plt.plot([1, 2, 3], [11, 22, 3])
plt.title(r'$\sigma_i=15$')

fig = plt.figure(3)
ax = fig.add_subplot(2, 2, 1)
ax.scatter([1, 3, 2], [3, 1, 2])
ax.scatter(1.5, 1.5)
ax = fig.add_subplot(2, 2, 4)
ax.plot([1, 2, 3], [1, 2, 3])



import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

Path = mpath.Path
path_data = [
    (Path.MOVETO, (1.58, -2.57)),
    (Path.CURVE4, (0.35, -1.1)),
    (Path.CURVE4, (-1.75, 2.0)),
    (Path.CURVE4, (0.375, 2.0)),
    (Path.LINETO, (0.85, 1.15)),
    (Path.CURVE4, (2.2, 3.2)),
    (Path.CURVE4, (3, 0.05)),
    (Path.CURVE4, (2.0, -0.5)),
    (Path.CLOSEPOLY, (1.58, -2.57)),
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)

# plot control points and connecting lines
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')

ax.grid()
ax.axis('equal')
plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)