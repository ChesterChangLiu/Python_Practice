import PIL
from PIL import Image

img = Image.open('/Users/arhumsultana/Desktop/ITEC1610/silk.png')
bw = img.convert('L')
bw.show()
bw.save('/Users/arhumsultana/Desktop/ITEC1610/silk_gray.png')
