import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#read an image from dictionary
img = cv.imread('/home/tuannghust/ImagesProcessing/ImagesProcessing/Lena.png')
#show image on a window
cv.imshow('Lena',img)
# plt.hist(img.ravel(),256,[0,256]); plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
