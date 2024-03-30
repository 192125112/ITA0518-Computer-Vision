import cv2
image=cv2.imread("C:/Users/neeru/OneDrive/Pictures/Saved Pictures/OIP (1).jpg")
k_size=(5,5)
sigma_x=0
blurred_imagecv2=cv2.GaussianBlur(image,k_size,sigma_x)
cv2.imwrite('blurred_imagecv2.jpg',blurred_imagecv2)
cv2.imshow('Original Image',image)
cv2.imshow('Blurred Imagecv2',blurred_imagecv2)
cv2.waitKey(0)
cv2.destroyAllWindows()
