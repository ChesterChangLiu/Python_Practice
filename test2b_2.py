import PIL
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import matplotlib

img=plt.imread("/Users/liuchang/Desktop/ITEC_1610/a2/2a_me_gray.png")
plt.hist(img.ravel(), bins=256, range=(0.0, 1.0), fc=(1., .8, 1.), ec=(1., 0.5, 1.)) 
plt.title("Histogram")
plt.xlabel("Grayscale Value")
plt.ylabel("No of pixels")
plt.show()

