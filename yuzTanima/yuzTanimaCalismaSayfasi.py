# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 20:36:56 2020

@author: 132415621
"""

import face_recognition
from PIL import Image

resim = Image.open('neseli-gunler.jpeg')

resim.show()

resimNeseliGunler = face_recognition.load_image_file("neseli-gunler.jpeg")

#%%
face_locations = face_recognition.face_locations(resimNeseliGunler)

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("Yeni bir yüz bulduk ve resimdeki yeri piksel olarak Üst: {}, Sol: {}, Alt: {}, Sağ: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = resimNeseliGunler[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()