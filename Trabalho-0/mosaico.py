import cv2 as cv
import numpy as np

imgpath = "img/baboon.png"
img = cv.imread(imgpath)
try:
    newimg = img.copy()

    mosaico = []
    fracao = 4                         
    tam = int(len(img)/fracao)

    for y in range(fracao):
        for x in range(fracao):
            mosaico.append((img[y*tam:y*tam+tam , x*tam:x*tam+tam]).astype(np.uint8))
        
    np.random.shuffle(mosaico)

    for y in range(fracao):
        for x in range(fracao):
            newimg[y*tam:y*tam+tam,x*tam:x*tam+tam] = mosaico[y*fracao+x]       # Mosaico 
        
    cv.imwrite("resultados/baboon-mosaico-random-"+str(fracao)+"x"+str(fracao)+".png",newimg)

    cv.imshow("Original",img)   
    cv.imshow("Mosaico "+str(fracao)+"x"+str(fracao),newimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")