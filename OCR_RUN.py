import pytesseract
import cv2
from PIL import Image
import numpy as np
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
#code that prevents error
def ocr_from_img(path):
    stream = open(path, "rb")
    bytes = bytearray(stream.read())
    numpyarray = np.asarray(bytes, dtype=np.uint8)
    #한글경로 오류 방지 코드
    img = cv2.imdecode(numpyarray, cv2.IMREAD_UNCHANGED)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

    # image = Image.open(path).convert('L')


    text= pytesseract.image_to_string(adaptive_threshold,lang='eng')
    print(text)
    return text
print(ocr_from_img(r'C:\Users\oh\Desktop\ocr.png'))