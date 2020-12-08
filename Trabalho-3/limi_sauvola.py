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
    k = 0.05
    R = 128

    newimg = limi.sauvola(img,n,0.5,R)*255

    cv.imshow("Imagem Sauvola com n = " + str(n) + " e k = " + str(k),newimg)

    aux = np.sum(newimg)/(img.shape[0]*img.shape[1])
    print("Fracao de pixels pretos utilizando metodo de Sauvola com K="+str(k)+":",format(100*aux/255,'.2f'),"%")

    cv.imwrite('resultados/sauvola_k='+str(k)+'_'+imgname,newimg)

    for k1 in range(1,10,1):
        k = k1/10
        newimg = limi.sauvola(img,n,k,R)*255

        cv.imshow("Imagem Sauvola com n = " + str(n) + " e k = " + str(k),newimg)

        aux = np.sum(newimg)/(img.shape[0]*img.shape[1])
        print("Fracao de pixels pretos utilizando metodo de Sauvola com K="+str(k)+":",format(100*aux/255,'.2f'),"%")

        cv.imwrite('resultados/sauvola_k='+str(k)+'_'+imgname,newimg)

    cv.waitKey(0)
    cv.destroyAllWindows()

    if plot_hist == 1:
        limi.plotar_histograma(img)


except:
    print("Imagem " + imgname + " não existe na pasta img")

