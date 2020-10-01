import cv2 as cv
import numpy as np
import sys

imgname = sys.argv[1]
imgpath = "img/" + imgname

try:
    img = cv.imread(imgpath)

    negimg = (255-img).astype(np.uint8)    # Negativo

    respath = "resultados/negativos/negativo-" + imgname
    cv.imwrite(respath,negimg)

    print("Resultado salvo em:",respath)

    cv.imshow("Original",img)
    cv.imshow("Negativa",negimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")
