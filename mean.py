import cv2 
from PIL import Image
img = cv2.imread("bird.png",0)
cv2.imshow('Greyscale',img)
blur = cv2.blur(img,(5,5))
cv2.imshow('Mean filter Processing',blur)
img.show()