import cv2 as cv
import numpy as np
import sys
from filtros_lib import filtros

imgname = sys.argv[1]
imgpath = "img/" + imgname

filtroindex = int(sys.argv[2])-1

try:
    img = cv.imread(imgpath)

    newimg = cv.filter2D(img,-1,filtros[filtroindex],cv.BORDER_CONSTANT)
    
    cv.imshow("Imagem original",img)
    cv.imshow("Filtro com borda constante h"+str(filtroindex+1),newimg)

    respath = "resultados/h" + str(filtroindex+1) + "-borda_constante-" + imgname
    cv.imwrite(respath,newimg)

    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada ou o filtro escolhido não está definido")