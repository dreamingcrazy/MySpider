import subprocess
orc = subprocess.Popen('C:\\Program Files (x86)\\Tesseract-OCR\\tesseract ./p1.jpg ./a')
print(orc)
import pytesseract
from PIL import Image

image = Image.open('p1.jpg')
# C:\Program Files (x86)\Tesseract-OCR
text = pytesseract.image_to_string(image)
print(text)