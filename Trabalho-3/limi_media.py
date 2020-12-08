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


    k = 0

    for n in range(5,21,3):

        newimg = limi.niblak(img,n,k)*255

        aux = np.sum(newimg)/(img.shape[0]*img.shape[1])
        print("Fracao de pixels pretos utilizando metodo da Media com n="+str(n)+":",format(100*aux/255,'.2f'),"%")

        cv.imwrite('resultados/media_n='+str(n)+'_'+imgname,newimg)

        cv.imshow("Imagem pelo metodo da media com n="+str(n),newimg)

    cv.waitKey(0)
    cv.destroyAllWindows()

    if plot_hist == 1:
        limi.plotar_histograma(img)

except:
    print("Imagem " + imgname + " não existe na pasta img")

