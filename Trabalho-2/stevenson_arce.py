import cv2 as cv
import numpy as np
import sys
from meio_tom_lib import *

imgname = sys.argv[1]
imgpath = "img/" + imgname


try:
    img = cv.imread(imgpath)

    newimg1 = stevenson_arce_1(img)*255
    newimg2 = stevenson_arce_2(img)*255

    cv.imshow("Imagem original",img)
    cv.imshow("Stevenson e Arce metodo 1",newimg1)
    cv.imshow("Stevenson e Arce metodo 2",newimg2)

    print("")

    cv.imwrite('resultados/stevenson_arce/stevenson_arce_1-'+imgname,newimg1)
    cv.imwrite('resultados/stevenson_arce/stevenson_arce_2-'+imgname,newimg2)

    print("Resultados salvos em:")
    print('resultados/stevenson_arce/stevenson_arce_1-'+imgname)
    print('resultados/stevenson_arce/stevenson_arce_2-'+imgname)

    cv.waitKey(0)
    cv.destroyAllWindows()
    
except:
    print("Erro")