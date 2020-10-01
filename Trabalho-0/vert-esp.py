import cv2 as cv
import numpy as np
import sys

imgname = sys.argv[1]
imgpath = "img/" + imgname

try:
    img = cv.imread(imgpath)

    newimg = np.flip(img,axis=0)       # Espelhamento vertical

    respath = "resultados/espelhadas-verticalmente/espelhada-"+imgname
    cv.imwrite(respath,newimg)

    print("Resultado salvo em:",respath)

    cv.imshow("Original",img)
    cv.imshow("Espelhada",newimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")
