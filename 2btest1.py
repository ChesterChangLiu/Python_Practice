import PIL
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


img = Image.open('/Users/liuchang/Desktop/ITEC_1610/a2/2a_me_gray.png')
histogram, bin_edges = np.histogram(img, bins=256, range=(0.0, 1.0))
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
plt.xlim([0.0, 1.0])  # <- named arguments do not work here

plt.plot(bin_edges[0:-1], histogram)  # <- or here
plt.show()
