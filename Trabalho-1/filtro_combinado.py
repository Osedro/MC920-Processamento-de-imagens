import cv2 as cv
import numpy as np
import sys
from filtros_lib import filtros

imgname = sys.argv[1]
imgpath = "img/" + imgname

try:
    img = cv.imread(imgpath)

    newimg3 = cv.filter2D(img,-1,filtros[2]).astype(np.uint8)
    newimg4 = cv.filter2D(img,-1,filtros[3]).astype(np.uint8)

    imgfinal = np.sqrt((newimg3**2)+(newimg4**2)).astype(np.uint8)

    cv.imshow("Imagem original",img)
    cv.imshow("Filtro combinado entre h3 e h4",imgfinal)

    respath = "resultados/combinado-" + imgname
    cv.imwrite(respath,imgfinal)

    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada ou o filtro escolhido não está definido")