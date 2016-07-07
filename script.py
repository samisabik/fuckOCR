#!/usr/bin/env python
import picamera,os,sys,time,Image
from PIL import Image,ImageFilter,ImageEnhance
import pytesseract

left = 1050
top = 1000
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
        time.sleep(5)
        camera.capture('output/image.jpg')
        im = Image.open("output/image.jpg")
        im = im.crop(box)
        im.save("output/edit.jpg")
        text = pytesseract.image_to_string(im)
        if text != "":
                print text
                text_file = open("output/text.txt", "w")
                text_file.write(text)
                text_file.close()
                os.system('lp -d Star-TUP900-STR-T-U001 -o PresenterAction=4NoLoopNoHoldEject output/text.txt')
        else:
                sys.exit()