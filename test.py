import Image,sys
from PIL import Image
import pytesseract
from PIL import ImageFilter


im = Image.open("image.jpg")
text = pytesseract.image_to_string(im)
if text != "":
	print "#" + text
	print "--------------------------"
else: 
	sys.exit()
