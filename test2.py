#%%
import pytesseract
from pytesseract import Output
import cv2
import os
from PIL import Image
from pytesseract.pytesseract import image_to_string
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

filename='./img/3.png'

# image=Image.open(filename)
img=cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img,cmap='gray')

text=image_to_string(img,lang='eng')
print('\n\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n')
print(text)
print(type(text))

text_file=open('OCR_text','a')
text_file.write(text)
text_file.close()



# %%
