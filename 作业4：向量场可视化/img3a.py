import matplotlib.pyplot as plt
import numpy as np

data = []
with open('jet.vecT') as f:
    next(f)
    for line in f.readlines():
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

w = 128
Y, X = np.mgrid[0:w:100j, 0:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
plt.streamplot(X, Y, U, V, density=[0.2, 0.3])
plt.savefig('img3a.jpg', dpi = 100)
plt.show()