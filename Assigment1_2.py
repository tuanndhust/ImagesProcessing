import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#img = cv.imread('/home/tuannghust/ImagesProcessing/ImagesProcessing/Lena.png',0)
def Histogram(img,bin):
    bin1 = []
    imgs = cv.imread(img,0)
    print(imgs.shape)
    imgss = imgs.flatten()
    #print(type(img))
    for i in range(bin+1):
        bin1.append(i)
    fig,ax = plt.subplots(1,1)
    ax.hist(imgss,bins=bin1)
    ax.set_title('Histogram of input image')
    plt.show()    
# def main():
#      Histogram('/home/tuannghust/ImagesProcessing/ImagesProcessing/Lena.png',255)
# if __name__ == "__main__":
#      main()
Histogram('/home/tuannghust/ImagesProcessing/ImagesProcessing/Lena.png',255)

