from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image = Image.open("image.jpg") # open colour image
# image.show() # show image

print(image.size)
print(image.format)
print(image.mode) 

# crop image
left = 50
top = 50
right = 500
bottom = 500
crop_image = image.crop((left, top, right, bottom))
plt.imshow(crop_image) # display data as an image

# rotate image
angle = 30
rotated_image = image.rotate(angle)
plt.imshow(rotated_image)

# Text Watermark
from PIL import ImageDraw, ImageFont
watermark_image = image.copy() # copy image
draw = ImageDraw.Draw(watermark_image) # create a drawing object
font = ImageFont.truetype("arial.ttf", size=100) # choose font
draw.text((0, 0), "Watermark", (0,0,0), font=font) # add text
plt.imshow(watermark_image)
#plt.show()

# Image Watermark
size = (500, 500)
crop_image = image.copy()
crop_image.thumbnail(size) # preserve aspect ratio

copied_image = image.copy()
copied_image.paste(crop_image, (0, 0)) # left top corner
plt.imshow(copied_image)
copied_image.show()

#Convert Image to Black and White
bw_image = image.convert("L") # convert to black and white
plt.imshow(bw_image, cmap="gray") #use cmap = "gray" for matplotlib to correctly show black and white
#bw_image.show()

#Convert to Different Formats
new_foramt_image = image.convert("HSV") #Hue Saturated Value
print(new_foramt_image.mode)

#Convert to Numpy Format
numpy_array = np.array(image)
print(numpy_array.shape)

numpy_image = Image.fromarray(numpy_array) # convert numpy array to image
plt.imshow(numpy_image)

