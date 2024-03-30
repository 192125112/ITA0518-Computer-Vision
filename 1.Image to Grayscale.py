import cv2
image=cv2.imread("C:/Users/neeru/OneDrive/Pictures/Camera Roll/PIc.jpg")
cv2.imshow('Original',image)
cv2.waitKey(0)
gray_image=cv.cvColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale',gray_image)
cv2.waitKey(0)
cv2.destroyALLWindows()
