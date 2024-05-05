import cv2
import numpy as np
def nothing(x):
    pass
#cv2.namedWindow('tracking')

while(True):
   frame= cv2.imread('\\Users\\drc\\Desktop\\\pto2.jpeg')
   hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   #HSA=V Stands for Hue,Saturation Value
   #hue refers to the color component, it has a range of 8 colors from blue, to magenta in a cirular ribbon og the cylinder
   #saturation means the depth of the color component
   #value stands for the brightness of the color component
   #this is for converting the colored image from BGR to HSV,  
   l_r=np.array([50,50,110])
   #this is for defining the lower limit for the color red,a numpy array is used to store the values
   u_r=np.array([255,255,130])
   #this is for defining the upper limit for the color red, a numpy array is used to store the values

   mask=cv2.inRange(hsv,l_r,u_r)
   #this is for threshholding the hsv image to get only the red colored part of the image 
   res=cv2.bitwise_and(frame,frame,mask=mask)
   #this is for masking the original image using the bitwise and 
   cv2.imshow('frame',frame)
   #this is for showing the original frame
   cv2.imshow('mask',mask)
   #this is for showing the mask
   cv2.imshow('res',res)
   #this is for showing the results of our operation

   key=cv2.waitKey(1) 
   if key==27:
       break
cv2.destroyAllWindows()   
   

