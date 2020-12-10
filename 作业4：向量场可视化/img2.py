import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

data = []
with open('jet.vecT') as f:
    next(f)
    for line in f:
        temp = line.split()
        data.append(temp)

x = []
y = []
for line in data:
    for i, item in enumerate(line):
        line[i] = float(item)
        if i % 2 != 0:
            x.append(line[i])
        else:
            y.append(line[i])
Y, X = np.mgrid[0:128:128j, 0:128:128j]
dx = np.asarray(x)
dy = np.asarray(y)
plt.figure(figsize = (7, 7))
plt.quiver(X, Y, dx, dy, color = 'blue')
plt.savefig('img2.jpg', dpi = 100)
plt.show()