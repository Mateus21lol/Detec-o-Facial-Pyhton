# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 16:44:05 2020

@author: Mateus Nobre Silva Almeida
"""


import cv2

listaimagens = ["imagem1.png","imagem2.jpg" ,"imagem3.png", "imagem4.png", "imagem5.png", "imagem6.png",
 "imagem7.png", "imagem8.png", "imagem9.png", "imagem10.png", "imagem11.png", "imagem12.png", "imagem13.jpg"]
i = 0
while i < 13:
    image_path = 'imagensselecionar/' + listaimagens[i]  # imagem
    cascade_path = 'haarcascade_frontalface_defalt.xml'  # arquivo de cascade
    clf = cv2.CascadeClassifier(cascade_path)  # cria o classificador
    img = cv2.imread(image_path)  # ler a imagem
    img = cv2.resize(img, (900, 700))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converter para preto e branco / grayscale
    faces = clf.detectMultiScale(gray, 1.1, 10)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)  # desenha um rec
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if(i == 11):
        i = 0
    else:
        i = i + 1
