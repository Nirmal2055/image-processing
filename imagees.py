from PIL import Image
import numpy as np
imge = Image.open('image1.jpeg')
imge.show('image1.jpeg')
img = Image.open('image1.jpeg').convert('L')
img.save('greyscale.jpeg')
print(np.array(img))
img.show('greyscale.jpeg')



# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# def rgb2gray(rgb):
#     return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

# img = mpimg.imread('image1.jpeg')

# gray = rgb2gray(img)

# plt.imshow(gray, cmap = plt.get_cmap('gray'))

# plt.savefig('lena_greyscale.png')
# plt.show()

    




# import numpy as np
# import matplotlib.pyplot as plt
# %matplotlib inline
# plt.rcParams['image1.cmap'] = 'gray'
# np.random.seed(0)

# def to_grayscale(im):
#     tile = np.tile(np.c_[0.333, 0.333, 0.333], reps=(im.shape[0],im.shape[1],1))
#     return np.sum(tile * im, axis=2)

# images = np.random.randint(0, 255, 24).reshape(2, 2, 2, 3)
# images.shape

