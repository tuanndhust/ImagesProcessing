from cv2 import sqrt
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('/home/tuanhust/Pictures/sugoku.png',0)
laplacian = cv.Laplacian(img,cv.CV_64F)
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
mag = sqrt(sobelx*sobelx+sobely*sobely)
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(mag,cmap = 'gray')
plt.title('Mag'), plt.xticks([]), plt.yticks([])
plt.show()