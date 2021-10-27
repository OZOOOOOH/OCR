import pytesseract
from pytesseract import Output
import cv2
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"

# 이미지를 불러와 gray 스케일로 변환해 준다.

image = cv2.imread('./img/OCR_ex.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)










# pytesseract에서는 numpy array를 읽지 못하고 file을 읽기 때문에 os로 파일을 불러들여야 한다.
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# pytesseract의 image to string을 써준다.
# 숫자니까 lang = 'None'으로

text = pytesseract.image_to_string(Image.open(filename), lang='eng')
os.remove(filename)

# 결과를 보자.

print(text)
cv2.imshow('', image)
