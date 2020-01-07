import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('noise.jpg',0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
equ = cv.equalizeHist(img)
res = np.hstack((img,equ)) 
cv.imwrite('res.jpeg',res)
plt.show()
img.show('res.jpeg')