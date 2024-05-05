import cv2
import numpy as np
#in this program whenever we left click at a point, a very small circle is drawn as a point, 
#when a second point is drawn, a line is drawn to connect this two points  
def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,255,255),-1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-1],points[-2],(0,255,0),2)
        cv2.imshow('image',img)


img=np.zeros((512,512,3),np.uint8)
points=[]
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()