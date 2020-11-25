import cv2 as cv
import numpy as np
import sys
from meio_tom_lib import *

imgname = sys.argv[1]
imgpath = "img/" + imgname


try:
    img = cv.imread(imgpath)

    newimg1 = burkes_1(img)*255
    newimg2 = burkes_2(img)*255

    cv.imshow("Imagem original",img)
    cv.imshow("Burkes metodo 1",newimg1)
    cv.imshow("Burkes metodo 2",newimg2)

    print("")

    cv.imwrite('resultados/burkes/burkes_1-'+imgname,newimg1)
    cv.imwrite('resultados/burkes/burkes_2-'+imgname,newimg2)

    print("Resultados salvos em:")
    print('resultados/burkes/burkes_1-'+imgname)
    print('resultados/burkes/burkes_2-'+imgname)

    cv.waitKey(0)
    cv.destroyAllWindows()
    
except:
    print("Erro")