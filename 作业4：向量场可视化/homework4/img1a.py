import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

a = np.loadtxt('jetMag.txt')

cm = LinearSegmentedColormap.from_list('br', ['b', 'r'])
plt.matshow(a, cmap = cm)

plt.savefig("img1a.jpg")
plt.show()
