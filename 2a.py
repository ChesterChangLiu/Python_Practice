import PIL
from PIL import Image

img = Image.open('/Users/liuchang/Desktop/ITEC_1610/a2/2a_me.png')
img.show()
a = img.convert('L')
a.show()
a.save('/Users/liuchang/Desktop/ITEC_1610/a2/2a_me_gray.png')
