from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageEnhance

image = Image.open("image.jpg")
plt.figure(figsize=(10,10))
image_color_enhance = image.copy()
image1 = ImageEnhance.Color(image_color_enhance).enhance(0.5)
image2 = ImageEnhance.Contrast(image_color_enhance).enhance(0.5)
image3 = ImageEnhance.Brightness(image_color_enhance).enhance(0.5)
image4 = ImageEnhance.Sharpness(image_color_enhance).enhance(0.5)
plt.subplot(2,2,1)
plt.imshow(image1)
plt.title("Color")
plt.subplot(2,2,2)
plt.imshow(image2)
plt.title("Contrast")   
plt.subplot(2,2,3)
plt.imshow(image3)
plt.title("Brightness")
plt.subplot(2,2,4)
plt.imshow(image4)
plt.title("Sharpness")
plt.show()