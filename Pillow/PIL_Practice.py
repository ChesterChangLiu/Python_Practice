from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image = Image.open("image.jpg") # open colour image
#image.show() # show image

print(image.size)
print(image.format)
print(image.mode) 

# crop image

left = 50
top = 50
right = 500
bottom = 500
crop_image = image.crop((left, top, right, bottom))
plt.imshow(crop_image)
crop_image.show()



