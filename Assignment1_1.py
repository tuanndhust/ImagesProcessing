import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#read an image from dictionary
img = cv.imread('/home/tuannghust/ImagesProcessing/ImagesProcessing/Lena.png')
#show image on a window
cv.imshow('Lena',img)
#replace blue channel of image
img[:,:,0] = 0
cv.imwrite('Lena_blue.png', img)



cv.waitKey(0)
cv.destroyAllWindows()
