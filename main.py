import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('sample.jpg')
kernel = np.ones((5,5),np.float32)
a = kernel / 25
dst = cv.filter2D(img,-1,a)
plt.subplot(121),plt.imshow(img),plt.title('1')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('2')
plt.xticks([]), plt.yticks([])
plt.show()
