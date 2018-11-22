import cv2 as cv
import pytesseract
import subprocess
import numpy as np


img = cv.imread('./p1.jpg')
cv.namedWindow('Image')
cv.imshow('Image',img)
cv.waitKey(10)
cv.destroyAllWindows()

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 转灰度图像
_,inv = cv.threshold(img,150,255,cv.THRESH_BINARY_INV)
# 转为黑白

print(inv)
for i in range(len(inv)):
    # i 为每一行
    for j in range(len(inv[i])):
        # j为每一列
        print(inv[i][j])
        if (inv[i][j] == np.array([255, 255, 255])).all():
            # 颜色为白色
            count = 0
            for k in range(-2,3):
                for l in range(-2,3):
                    try:
                        if (inv[i+k][j+l] == 255).all():
                            count += 1
                    except IndexError:
                        pass
            if count <=6:
                # 周围少于货等于6个白点
                inv[i][j] = 0

dilation = cv.dilate(inv,(8,8),iterations=1)
# 图形加粗

cv.imwrite('./zhuan.jpg',dilation)
child = subprocess.Popen('C:\\Program Files (x86)\\Tesseract-OCR\\tesseract zhuan.jpg result')
child.wait()
text = open('result.txt').read().strip()
print(text)