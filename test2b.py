import PIL
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np


 
img = plt.imread('/Users/liuchang/Desktop/ITEC_1610/a2/2a_me_gray.png')



plt.hist(img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
#calculating histogram



plt.show()
