import cv2 as cv
import numpy as np
import sys
from filtros import *

imgname = sys.argv[1]
imgpath = "img/" + imgname

filtroindex = int(sys.argv[2])-1

try:
    img = cv.imread(imgpath)

    newimg = cv.filter2D(img,-1,filtros[filtroindex])


    cv.imshow("Imagem original",img)
    cv.imshow("Filtro h"+str(filtroindex+1),newimg)


    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada ou o filtro escolhido não está definido")