import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def Histogram(img,bin):
    bin1 = np.arange(bin+1)
    imgs = cv.imread(img)
    #print(imgs)
    #print(imgs.shape)
    #print(imgs[:,:,2])
    #number channels of images
    dims = imgs.ndim
    if dims == 1:
        imgss = imgs.flatten()
    #print(type(img))
    # for i in range(bin+1):
    #     bin1.append(i)
        fig,ax = plt.subplots(1,1)
        ax.hist(imgss,bins=bin1)
        ax.set_title('Histogram of input image')
    elif dims == 3:
        #blue channel
        fig, (ax, ax1, ax2) = plt.subplots(1,3)
        b = imgs[:,:,0]
        bs = b.flatten()
        ax.hist(bs,bins=bin1)
        ax.set_title('blue')  
        #grown channel
        g = imgs[:,:,1]
        gs = g.flatten() 
        ax1.hist(gs,bins=bin1)
        ax1.set_title('grown')
        #red channel
        r = imgs[:,:,2]
        rs = r.flatten() 
        ax2.hist(rs,bins=bin1)
        ax2.set_title('red')    
    plt.show()    

Histogram('/home/tuannghust/ImagesProcessing/ImagesProcessing/Lena.png',255)
