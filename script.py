#!/usr/bin/env python
import picamera,os,sys,time
import Image,sys
from PIL import Image
import pytesseract
from PIL import ImageFilter
import Image,sys
from PIL import Image
from PIL import ImageEnhance
import pytesseract
from PIL import ImageFilter

left = 900
top = 850
width = 1000
height = 200
box = (left, top, left+width, top+height)

camera = picamera.PiCamera()
camera.resolution = (2592, 1944)

seed = raw_input("enter your seed: ")
text_file = open("output/text.txt", "w")
text_file.write(seed)
text_file.close()
os.system('lp -d Star-TUP900-STR-T-U001 -o PresenterAction=4NoLoopNoHoldEject output/text.txt')

while True:
        time.sleep(10)
        camera.capture('output/image.jpg')
        im = Image.open("output/image.jpg")
        im = im.crop(box)
        enhancer = ImageEnhance.Contrast(imc)
        im = enhancer.enhance(5)
        text = pytesseract.image_to_string(im)
        if text != "":
                text_file = open("output/text.txt", "w")
                text_file.write(text)
                text_file.close()
                os.system('lp -d Star-TUP900-STR-T-U001 -o PresenterAction=4NoLoopNoHoldEject output/text.txt')
        else:
                sys.exit()