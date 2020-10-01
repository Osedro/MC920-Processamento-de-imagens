import cv2 as cv
import numpy as np
import sys

imgname = sys.argv[1]
fracao = int(sys.argv[2])
imgpath = "img/" + imgname


try:
    img = cv.imread(imgpath)
    newimg = img.copy()

    mosaico = []
    tam = int(len(img)/fracao)

    for y in range(fracao):
        for x in range(fracao):
            mosaico.append((img[y*tam:y*tam+tam , x*tam:x*tam+tam]).astype(np.uint8))
        
    np.random.shuffle(mosaico)

    for y in range(fracao):
        for x in range(fracao):
            newimg[y*tam:y*tam+tam,x*tam:x*tam+tam] = mosaico[y*fracao+x]       # Mosaico 
        
    respath = "resultados/mosaicos/mosaico-" + str(fracao) + "x" + str(fracao) + "-" + imgname
    cv.imwrite(respath,newimg)

    print("Resultado salvo em:",respath)

    cv.imshow("Original",img)   
    cv.imshow("Mosaico "+str(fracao)+"x"+str(fracao),newimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")