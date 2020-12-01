import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def mediana(img,n):
    newimg = np.zeros(img.shape)

    if n%2 == 1:
        n = n - 1


    for i in range(len(img)):
        for j in range(len(img[i])):

            leftlim = int(j - (n/2))
            rightlim = int(j + (n/2))

            uplim = int(i - (n/2))
            downlim = int(i + (n/2))

            if leftlim < 0:
                leftlim = 0

            if rightlim > img.shape[1]:
                rightlim = img.shape[1]

            if uplim < 0:
                uplim = 0

            if downlim > img.shape[0]:
                downlim = img.shape[0]

            l = img[uplim:downlim,leftlim:rightlim]
            
            T = np.median(l)

            if img[i][j] > T:
                newimg[i][j] = 1
            else:
                newimg[i][j] = 0

            
    return newimg.astype(np.uint8)

def contraste(img,n):
    newimg = np.zeros(img.shape)

    if n%2 == 1:
        n = n - 1


    for i in range(len(img)):
        for j in range(len(img[i])):

            leftlim = int(j - (n/2))
            rightlim = int(j + (n/2))

            uplim = int(i - (n/2))
            downlim = int(i + (n/2))

            if leftlim < 0:
                leftlim = 0

            if rightlim > img.shape[1]:
                rightlim = img.shape[1]

            if uplim < 0:
                uplim = 0

            if downlim > img.shape[0]:
                downlim = img.shape[0]

            l = img[uplim:downlim,leftlim:rightlim]

            pixmax = int(l.max())
            pixmin = int(l.min())

            if img[i][j] - pixmin > pixmax - img[i][j]:
                newimg[i][j] = 1
            else:
                newimg[i][j] = 0

            
    return newimg.astype(np.uint8)

def phansalskar(img,n,k,R,p,q):
    newimg = np.zeros(img.shape)

    if n%2 == 1:
        n = n - 1


    for i in range(len(img)):
        for j in range(len(img[i])):

            leftlim = int(j - (n/2))
            rightlim = int(j + (n/2))

            uplim = int(i - (n/2))
            downlim = int(i + (n/2))

            if leftlim < 0:
                leftlim = 0

            if rightlim > img.shape[1]:
                rightlim = img.shape[1]

            if uplim < 0:
                uplim = 0

            if downlim > img.shape[0]:
                downlim = img.shape[0]

            l = img[uplim:downlim,leftlim:rightlim]

            media = float(np.average(l))
            dp = float(np.std(l))
            
            
            T = int(media*(1 + (k*((dp/R)-1)) + (p*np.exp((-q)*media))))            

            if img[i][j] > T:
                newimg[i][j] = 1
            else:
                newimg[i][j] = 0

            
    return newimg.astype(np.uint8)

def sauvola(img,n,k,R):
    newimg = np.zeros(img.shape)

    if n%2 == 1:
        n = n - 1


    for i in range(len(img)):
        for j in range(len(img[i])):

            leftlim = int(j - (n/2))
            rightlim = int(j + (n/2))

            uplim = int(i - (n/2))
            downlim = int(i + (n/2))

            if leftlim < 0:
                leftlim = 0

            if rightlim > img.shape[1]:
                rightlim = img.shape[1]

            if uplim < 0:
                uplim = 0

            if downlim > img.shape[0]:
                downlim = img.shape[0]

            l = img[uplim:downlim,leftlim:rightlim]

            media = float(np.average(l))
            dp = float(np.std(l))
            
            
            T = int(media*(1+(k*((dp/R)-1))))            


            if img[i][j] > T:
                newimg[i][j] = 1
            else:
                newimg[i][j] = 0

            
    return newimg.astype(np.uint8)

def niblak(img,n,k):
    newimg = np.zeros(img.shape)

    if n%2 == 1:
        n = n - 1


    for i in range(len(img)):
        for j in range(len(img[i])):

            leftlim = int(j - (n/2))
            rightlim = int(j + (n/2))

            uplim = int(i - (n/2))
            downlim = int(i + (n/2))

            if leftlim < 0:
                leftlim = 0

            if rightlim > img.shape[1]:
                rightlim = img.shape[1]

            if uplim < 0:
                uplim = 0

            if downlim > img.shape[0]:
                downlim = img.shape[0]

            l = img[uplim:downlim,leftlim:rightlim]

            media = float(np.average(l))
            dp = float(np.std(l))
            
            
            T = int(media+k*dp)
            


            if img[i][j] > T:
                newimg[i][j] = 1
            else:
                newimg[i][j] = 0

            
    return newimg.astype(np.uint8)

def bernsen(img,n):
    newimg = np.zeros(img.shape)

    if n%2 == 1:
        n = n - 1


    for i in range(len(img)):
        for j in range(len(img[i])):

            leftlim = int(j - (n/2))
            rightlim = int(j + (n/2))

            uplim = int(i - (n/2))
            downlim = int(i + (n/2))

            if leftlim < 0:
                leftlim = 0

            if rightlim > img.shape[1]:
                rightlim = img.shape[1]

            if uplim < 0:
                uplim = 0

            if downlim > img.shape[0]:
                downlim = img.shape[0]

            l = img[uplim:downlim,leftlim:rightlim]
            #print(l)

            pixmax = int(l.max())
            pixmin = int(l.min())
            
            
            T = int((pixmax+pixmin)/2)
            


            if img[i][j] > T:
                newimg[i][j] = 1
            else:
                newimg[i][j] = 0

            
    return newimg.astype(np.uint8)

def plotar_histograma(img,T):
    plt.hist(img.ravel(),256,[0,256]) 
    plt.axvline(x=T,ymax=np.max(cv.calcHist([img],[0],None, [256], [0,256])), color = "red")
    plt.show()

def limi_global(img, T):
    new = img.copy()
    new = img[:][:]>T
    return (new*1).astype(np.uint8)

def ridler_calvard(img):

    num_pixel = (img.shape[0]*img.shape[1])
    hist = cv.calcHist([img],[0],None, [256], [0,256])
    T = int(np.sum(img)/num_pixel)

    dif = 100

    while dif > 1 or dif < -1:

        mi1 = 0
        soma = 0

        for i in range(T):
            mi1 = mi1 + i*hist[i]
            soma = soma + hist[i]

        mi1 = mi1/soma

        mi2 = 0
        soma = 0
        for i in range(T,256):
            mi2 = mi2 + i*hist[i]
            soma = soma + hist[i]

        mi2 = mi2/soma
        
        dif = T - (mi1+mi2)/2
        print(dif)
        T = int((mi1+mi2)/2)

    return T