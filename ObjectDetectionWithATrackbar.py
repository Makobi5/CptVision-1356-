import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('tracking')
#this window is for altering the color saturation values
#defining the trackbars for the  lower bound on Hue, saturation and values
cv2.createTrackbar('LH','tracking',0,255,nothing)
cv2.createTrackbar('LS','tracking',0,255,nothing)
cv2.createTrackbar('LV','tracking',0,255,nothing)
#the initial lower value is set to 0 for each of the above 

#defining the trackbars for the  upper bound on Hue, saturation and values
cv2.createTrackbar('UH','tracking',255,255,nothing)
cv2.createTrackbar('US','tracking',255,255,nothing)
cv2.createTrackbar('UV','tracking',255,255,nothing)

#the initial upper value is set to 255 for each of the above
while True:
    frame=cv2.imread('\\Users\\drc\\Desktop\\\pto2.jpeg')
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #getting values from the track bar
    lower_hue=cv2.getTrackbarPos('LH','tracking')
    lower_saturation=cv2.getTrackbarPos('LS','tracking')
    lower_value=cv2.getTrackbarPos('LV','tracking')

    upper_hue=cv2.getTrackbarPos('UH','tracking')
    upper_saturation=cv2.getTrackbarPos('US','tracking')
    upper_value=cv2.getTrackbarPos('UV','tracking')

    lowerRed=np.array([lower_hue,lower_saturation,lower_value])
    upperRed=np.array([upper_hue,upper_saturation,upper_value])
    mask=cv2.inRange(hsv,lowerRed,upperRed)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()  