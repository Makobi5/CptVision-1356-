import cv2
img=cv2.imread('\\Users\\drc\\Desktop\\mariana.jpg',1)
img2=cv2.imread('\\Users\\drc\\Desktop\\bunyonyi travels.png',1)
#cup=img[14:45,35:66]
#img[23:137,85:158]=cup

#using the add method
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
dst=cv2.add(img,img2)

#using the addweighted method
#here we can add percentage of how we want the images to be added
dst2=cv2.addWeighted(img,.1,img2,.9,0)
cv2.imshow('image',dst2)


cv2.waitKey(0)

cv2.destroyAllWindows()