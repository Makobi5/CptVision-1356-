import cv2
import numpy as np
# img=cv2.imread('\\Users\\drc\\Desktop\\python programs\\python2\\OpenCV\\folders\\hood.jpg',1)
img=np.zeros([512,512,3],np.uint8)
font=cv2.FONT_HERSHEY_DUPLEX
img=cv2.putText(img, "The Blackhood",(10,350),font,1,(0,0,255),2,cv2.LINE_AA)


cv2.imshow('frame',img)

cv2.waitKey(0)
cv2.destroyAllWindows()