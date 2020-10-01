import cv2 as cv
import numpy as np
import sys

imgname = sys.argv[1]
gamma = float(sys.argv[2])
imgpath = "img/" + imgname

try:
    img = cv.imread(imgpath)

    aux = img/255
    aux = aux**(1/gamma)
    newimg = (aux*255).astype(np.uint8)     # Correção gamma 

    respath = "resultados/correcao-gamma/gamma-" + str(gamma) + "-" + imgname
    cv.imwrite(respath,newimg)

    cv.imshow("Original",img)   
    cv.imshow("Correção gamma " + str(gamma),newimg)

    print("Resultado salvo em:",respath)
    
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")