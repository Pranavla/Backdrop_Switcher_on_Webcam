#Importing the libraries

import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

#Webcam
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
cam.set(cv2.CAP_PROP_FPS, 60)

#Assigning the function
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

#Importing the folder of images
listImg =os.listdir("F:\Computer_vision\Open cv\Backdrop_Switcher\BackgroundImages")
print(listImg)

imgList =[]
for imgPath in listImg:
    img = cv2.imread(f'F:\Computer_vision\Open cv\Backdrop_Switcher\BackgroundImages/{imgPath}')
    imgList.append(img)
print(len(imgList))

indexImg = 0


#Background changer
while True:
    success, img = cam.read()
    #imgOut = segmentor.removeBG(img, (0,0,0),threshold = 0.75)
    imgOut = segmentor.removeBG(img, imgList[indexImg],threshold = 0.85)

    cv2.imshow("Image", imgOut)
    key = cv2.waitKey(1)
    if key == ord('b'):
        if indexImg>0:
            indexImg -=1
    elif key == ord('f'):
        if indexImg <len(imgList)-1:
            indexImg +=1
    elif key == ord('q'):
        indexImg -=1
        break


