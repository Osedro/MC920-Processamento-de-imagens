import cv2 as cv
import numpy as np
import sys

imgname = sys.argv[1]
imgpath = "img/" + imgname

try:
    img = cv.imread(imgpath)

    newimg = img.copy()

    aux = newimg[0:int(len(newimg)/2)]
    aux = np.flip(aux,axis = 0)
    newimg[int(len(newimg)/2):int(len(newimg))] = aux.astype(np.uint8)       # Espelha as linhas da parte superior para a parte inferior

    respath = "resultados/espelhadas-centro/espelhada-centro-" + imgname
    cv.imwrite(respath,newimg)

    print("Resultado salvo em:",respath)

    cv.imshow("Original",img)   
    cv.imshow("Reflexao no centro",newimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")