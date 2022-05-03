import cv2
import numpy as np
import matplotlib.pyplot as plt

#gan anh
fn='/home/tuannghust/ImagesProcessing/ImagesProcessing/Lena.png'
img=cv2.imread(fn)
# cv2.imshow('anh vua nhap',img)
# cv2.waitKey(0)

img_gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#tinh histogram

hist=np.zeros((256,))
h,w=img_gray.shape[:2]
print ("kich thuoc anh w=",w,",h=",h)

for i in range(h):
    for j in range(w):    
        hist[img_gray[i][j]] +=1

#hien thi histogram
fig = plt.figure()
plt.plot(hist)
plt.show()
