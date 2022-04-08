from PIL import Image
import matplotlib.pyplot as plt


image1 = Image.open("image1.png")
image2 = Image.open("image2.png")
# Alpha Blending
# make sure the images have the same size
# make sure the images have the alpha channel: PNG

image1 = image1.copy()
image2 = image2.copy()

# make sure the images have the same size
image2 = image2.resize(image1.size)

# Blending
image_blend = Image.blend(image1, image2, 0.5)
plt.imshow(image_blend)
plt.show()
