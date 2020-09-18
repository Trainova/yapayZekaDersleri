# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 21:06:44 2020

@author: 132415621
"""
# yuklemeniz gereken program ve de kurma yeri: "C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

import pytesseract as tess

from PIL import Image

resim = Image.open("c:\yapayZeka\plakaOkuma\ocr_image_2.png") 

metin=tess.image_to_string(resim)

print("plaka numarasi: "+metin)

#%%

import pytesseract as tess

from PIL import Image

resim = Image.open("c:\yapayZeka\plakaOkuma\plaka.png") 

metin=tess.image_to_string(resim)

print("plaka numarasi: "+metin)

#%%

import pytesseract as tess

from PIL import Image

resim = Image.open("c:\yapayZeka\plakaOkuma\\numune_alma.png") 

metin=tess.image_to_string(resim)

print("resimde yazan metin: "+metin)

#%%

import pytesseract as tess

from PIL import Image

resim = Image.open("c:\yapayZeka\plakaOkuma\\merhaba_yz.png") 

metin=tess.image_to_string(resim)

print("resimde yazan metin: "+metin)