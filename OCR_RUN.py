import pytesseract
import cv2
from pathlib import Path


pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def ocr_from_img(path = './img/2.png',lang='eng'):
    file_name = Path(path).stem

    # image=Image.open(filename)
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

    # cv2.imshow('image', adaptive_threshold)
    # cv2.waitKey(0)

    text= pytesseract.image_to_string(adaptive_threshold,lang)
    print('\n\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n')
    print(text)
    return text
    # path_text='./text/'
    # text_file=open(path_text+f'OCR_{file_name}_text','a' ,-1, 'utf-8')
    # text_file.write(text)
    # text_file.close()


