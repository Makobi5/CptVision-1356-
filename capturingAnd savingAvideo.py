import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('myvideo2.avi', fourcc,20.0,(640,480))

while(True):
    ret, frame=cap.read()

    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
    if ret==True:
     cv2.imshow('frame',frame)
     out.write(frame)
     if cv2.waitKey(1) & 0xFF== ord('q'):
        break
    else:
       break 
cap.release()
out.release()
cv2.destroyAllWindows()    