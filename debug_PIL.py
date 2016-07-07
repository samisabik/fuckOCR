#!/usr/bin/env python
import Image,sys
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

left = 900
top = 800
width = 1000
height = 200
box = (left, top, left+width, top+height)

im = Image.open("output/image.jpg")
im = im.crop(box)
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(3)
im.save('output/out.jpg')
text = pytesseract.image_to_string(im)
if text != "":
        print text
else:
        sys.exit()