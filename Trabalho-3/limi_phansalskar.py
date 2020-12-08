import cv2 as cv
import numpy as np
import sys
import limi_lib as limi

imgname = sys.argv[1]

try:
    plot_hist = int(sys.argv[2])
except:
    plot_hist = 0

imgpath = "img/" + imgname


try:
    img = cv.imread(imgpath,0)

    imgname = imgname.split('.')[0]+'.png'

    cv.imshow("Imagem original",img)

    n = 15
    R = 25
    p = 2
    q = 10

    k = 0.05

    newimg = limi.phansalskar(img,n,k,R,p,q)*255

    cv.imshow("Imagem Phansalskar com n = " + str(n) + " e k = " + str(k),newimg)
    cv.imwrite('resultados/phansalskar_k='+str(k)+'_'+imgname,newimg)
    aux = np.sum(newimg)/(img.shape[0]*img.shape[1])
    print("Fracao de pixels pretos utilizando metodo de Phansalskar com K="+str(k)+":",format(100*aux/255,'.2f'),"%")

    k = 0.08

    newimg = limi.phansalskar(img,n,k,R,p,q)*255

    cv.imshow("Imagem Phansalskar com n = " + str(n) + " e k = " + str(k),newimg)
    cv.imwrite('resultados/phansalskar_k='+str(k)+'_'+imgname,newimg)
    aux = np.sum(newimg)/(img.shape[0]*img.shape[1])
    print("Fracao de pixels pretos utilizando metodo de Phansalskar com K="+str(k)+":",format(100*aux/255,'.2f'),"%")

    k = 0.1

    newimg = limi.phansalskar(img,n,k,R,p,q)*255

    cv.imshow("Imagem Phansalskar com n = " + str(n) + " e k = " + str(k),newimg)
    cv.imwrite('resultados/phansalskar_k='+str(k)+'_'+imgname,newimg)
    aux = np.sum(newimg)/(img.shape[0]*img.shape[1])
    print("Fracao de pixels pretos utilizando metodo de Phansalskar com K="+str(k)+":",format(100*aux/255,'.2f'),"%")

    k = 0.15

    newimg = limi.phansalskar(img,n,k,R,p,q)*255

    cv.imshow("Imagem Phansalskar com n = " + str(n) + " e k = " + str(k),newimg)
    cv.imwrite('resultados/phansalskar_k='+str(k)+'_'+imgname,newimg)
    aux = np.sum(newimg)/(img.shape[0]*img.shape[1])
    print("Fracao de pixels pretos utilizando metodo de Phansalskar com K="+str(k)+":",format(100*aux/255,'.2f'),"%")

    k = 0.2

    newimg = limi.phansalskar(img,n,k,R,p,q)*255

    cv.imshow("Imagem Phansalskar com n = " + str(n) + " e k = " + str(k),newimg)
    cv.imwrite('resultados/phansalskar_k='+str(k)+'_'+imgname,newimg)
    aux = np.sum(newimg)/(img.shape[0]*img.shape[1])
    print("Fracao de pixels pretos utilizando metodo de Phansalskar com K="+str(k)+":",format(100*aux/255,'.2f'),"%")

    k = 0.5

    newimg = limi.phansalskar(img,n,k,R,p,q)*255

    cv.imshow("Imagem Phansalskar com n = " + str(n) + " e k = " + str(k),newimg)
    cv.imwrite('resultados/phansalskar_k='+str(k)+'_'+imgname,newimg)
    aux = np.sum(newimg)/(img.shape[0]*img.shape[1])
    print("Fracao de pixels pretos utilizando metodo de Phansalskar com K="+str(k)+":",format(100*aux/255,'.2f'),"%")

    cv.waitKey(0)
    cv.destroyAllWindows()

    if plot_hist == 1:
        limi.plotar_histograma(img)

except:
    print("Imagem " + imgname + " não existe na pasta img")

