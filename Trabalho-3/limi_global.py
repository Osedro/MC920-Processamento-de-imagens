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
    imgname = imgname.split('.')[0]+'.png'
    img = cv.imread(imgpath,0)

    cv.imshow("Imagem original",img)


    T1 = limi.ridler_calvard(img)                           # Limiar utilizando o algoritmo de Ridler e Calvard
    T2 = int(np.sum(img)/(img.shape[0]*img.shape[1]))       # Limiar utilizando valor médio dos pixels
    
    

    

    print("Fracao de pixels pretos utilizando Ridler e Calvard: ",format(100*T1/255,'.2f'),"%")
    print("Fracao de pixels pretos utilizando media global: ",format(100*T2/255,'.2f'),"%")


    newimg1 = limi.limi_global(img,T1)*255
    newimg2 = limi.limi_global(img,T2)*255

    cv.imshow("Imagem global Ridler e Calvard",newimg1)
    cv.imshow("Imagem global media",newimg2)

    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imwrite('resultados/global_ridler_'+imgname,newimg1)
    cv.imwrite('resultados/global_media_'+imgname,newimg2)

    for t in range(T1-100,T1+100,10):
        if t > 0 and t < 256:
            newimg = limi.limi_global(img,t)*255
            print("Fracao de pixels pretos utilizando T = "+str(t)+":",format(100*t/255,'.2f'),"%")
            cv.imshow("Imagem global T = "+str(t),newimg)
            cv.waitKey(0)
            cv.destroyAllWindows()
            cv.imwrite('resultados/global_T='+str(t)+'_'+imgname,newimg)
    
    if plot_hist == 1:
        limi.plotar_histograma_t(img,T1)
        limi.plotar_histograma_t(img,T2)

    newimg1 = limi.limi_global(img,T1)*255
    newimg2 = limi.limi_global(img,T2)*255

except:
    print("Imagem " + imgname + " não existe na pasta img")

