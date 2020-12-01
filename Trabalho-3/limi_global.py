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

    cv.imshow("Imagem original",img)


    T1 = limi.ridler_calvard(img)                           # Limiar utilizando o algoritmo de Ridler e Calvard
    T2 = int(np.sum(img)/(img.shape[0]*img.shape[1]))       # Limiar utilizando valor médio dos pixels
    
    if plot_hist == 1:
        limi.plotar_histograma(img,T1)

    newimg1 = limi.limi_global(img,T1)*255
    newimg2 = limi.limi_global(img,T2)*255

    cv.imshow("Imagem global Ridler e Calvard",newimg1)
    cv.imshow("Imagem global media",newimg2)
    cv.waitKey(0)
    cv.destroyAllWindows()


    for t in range(T1-100,T1+100,10):
        if t > 0 and t < 256:
            newimg = limi.limi_global(img,t)*255
            cv.imshow("Imagem global T = "+str(t),newimg)
            cv.waitKey(0)
            cv.destroyAllWindows()

except:
    print("Imagem " + imgname + " não existe na pasta img")

