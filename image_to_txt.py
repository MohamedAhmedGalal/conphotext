# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 11:49:53 2024

@author: dell
"""

import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\Py programs\opencv_proj\tesseract\tesseract.exe'

#read image
# for i in range (1,9):
def convert(i):
    path=r"D:\Py programs\opencv_proj\pdf_img_to_txt\New folder\enhanced\b_{}.jpg".format(i)
    # Read image from which text needs to be extracted
    img = cv2.imread(path)# get grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #noise removal
    noise=cv2.medianBlur(gray,3)
    # thresholding# converting it to binary image by Thresholding
    # this step is require if you have colored image because if you skip this part
    # then tesseract won’t able to detect text correctly and this will give incorrect #result
    thresh = cv2.threshold(noise, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #Configuration
    config = ('-l eng — oem 3 — psm 3')
    # pytessercat
    text = pytesseract.image_to_string(thresh,config=config)
    # print(text)
    file = open(r"D:\Py programs\opencv_proj\pdf_img_to_txt\New folder\enhanced\out_txt_{}.txt".format(i), "w+")
    file.write("")
    file.close()
    
    file = open(r"D:\Py programs\opencv_proj\pdf_img_to_txt\New folder\enhanced\out_txt_{}.txt".format(i), "a")
    
    file.write(text)
    # Close the file
    file.close()
for i in range (1,10):
    convert(i)
