import cv2
from PIL import Image
image = cv2.imread("bird.jpg")
gauss = cv2.GaussianBlur(image,(7,7),0)
unsharp_image = cv2.addWeighted(image,2,gauss,-1,0)
cv2.imshow("high boost filtering", unsharp_image)