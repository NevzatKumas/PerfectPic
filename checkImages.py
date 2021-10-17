import os
import numpy
import cv2
import time

pictures = []
var1=0
var2=0


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

directory = "/Users/abedmiah/Documents/hackru-fall21/Images/"

i = 0

for filename in os.listdir(directory):
    if filename.endswith(".png"):
        filePath = directory + filename
        img = cv2.imread(filePath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
        i = 0 
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            i = i+1
            var1 = i
            j = 0
            for (x,y,w,h) in eyes:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                j = j+1
                var2=j
        cv2.imshow('image',img)
        cv2.imwrite("/Users/abedmiah/Documents/hackru-fall21/Images/temp_" + str(i) + ".png", img)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        data = (var1,var2, filePath)
        pictures.append(data)
        del data

print(len(pictures))

for i in range(len(pictures)):
    temp1 = pictures[0][0]
    temp2 = pictures[0][0]
    if (pictures[i][0] > temp1):
        temp1 = pictures[i][0]

