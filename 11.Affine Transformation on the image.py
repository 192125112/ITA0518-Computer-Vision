import cv2
import numpy as np
img = cv2.imread("C:/Users/neeru/OneDrive/Pictures/Saved Pictures/OIP (2).jpg")
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("Affine Transform", dst)
cv2.waitKey(0)
cv2.destroyAllWindows() 
