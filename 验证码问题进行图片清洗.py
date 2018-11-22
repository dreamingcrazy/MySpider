from PIL import Image
import subprocess

def clearnFile(file_path,newfilepath):
    image=Image.open(file_path)

    image = image.point(lambda x:0 if x<143 else 255)

    image.save(newfilepath)

    # subprocess.call(['C:\\Program Files (x86)\\Tesseract-OCR\\tesseract',newfilepath,'output'])
    subprocess.call(['C:\\Program Files (x86)\\Tesseract-OCR\\tesseract', '-1','chi_sim',newfilepath, 'output'])

    with open('output.txt','r') as f:
        print(f.read())

if __name__ == '__main__':
    clearnFile('./2.jpg','new.png')