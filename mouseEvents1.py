import cv2
#this program is for displaying x and y cordinates on the image when 
#a left click miouse event is perfomed anywhere
#however it displays color cordinates when we right click instead.

def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,' ',y)
        font=cv2.FONT_HERSHEY_DUPLEX
        strx=str(x) + ' ' + str(y)
        cv2.putText(img,strx,(x,y),font,1,(255,255,0),1)
        cv2.imshow('image',img)
        #adding code for a right click event
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]    #declaring a variable blue and using the image variable to access the blue channel
        #from BGR, blue has index 0
        green=img[y,x,1]
        red=img[y,x,2]   
        font=cv2.FONT_HERSHEY_DUPLEX
        strB=str(blue) + ' ' + str(green) +' '+ str(red)
        cv2.putText(img,strB,(x,y),font,1,(0,0,255),1)
        cv2.imshow('image',img) 
img=cv2.imread('\\Users\\drc\\Desktop\\mariana.jpg')  
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
