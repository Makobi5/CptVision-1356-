import cv2
cap=cv2.VideoCapture(0)
#the code lines below are for printing the height and width of the frame
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#the next two lines work just the same way like the previous two lines
print(cap.get(3)) #3 stands for frame width and 4 stands for frame height
print(cap.get(4))

#setting values for width and height
cap.set(3,1280)
cap.set(4,720)
#if we provide very large values for the width and the height, they will replaced by the above values because these are the
# maximum values for the width and height
#the above two lines will change the values of height and width to new
print(cap.get(3)) 
print(cap.get(4))
while(True):
    ret,frame=cap.read()
    if ret==True:
        #the line below converts the color of the video being captured to gray scale mode
        #it takes argumnets, name of the frame, and the color to be converted to
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
       break    

    
cap.release()
cv2.destroyAllWindows()    