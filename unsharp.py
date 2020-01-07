from PIL import Image
from pylab import *
from scipy.ndimage import filters





im = array(Image.open("bird.jpg").convert("L"), "f")


sigma = 3
blurred = filters.gaussian_filter(im,sigma)


weight = 0.25
unsharp = im - 0.25*blurred



figure()
imshow(im)
gray()
title("original image")

figure()
imshow(unsharp)
gray()
title("unsharp mask with weight {}".format(weight))

show()