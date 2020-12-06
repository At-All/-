import numpy as np
from PIL import Image

a = np.loadtxt('jetMag.txt')
print(a)
print(a.max(),a.min())
img = Image.fromarray(a);
img.show()