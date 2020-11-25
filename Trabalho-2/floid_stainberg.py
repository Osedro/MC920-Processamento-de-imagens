import cv2 as cv
import numpy as np
import sys
from meio_tom_lib import *

imgname = sys.argv[1]
imgpath = "img/" + imgname


try:
    img = cv.imread(imgpath)

    newimg1 = floid_stainberg_1(img)*255
    newimg2 = floid_stainberg_2(img)*255

    cv.imshow("Imagem original",img)
    cv.imshow("Floid e Stainberg metodo 1",newimg1)
    cv.imshow("Floid e Stainberg metodo 2",newimg2)

    print("")

    cv.imwrite('resultados/floid_stainberg/floid_stainberg_1-'+imgname,newimg1)
    cv.imwrite('resultados/floid_stainberg/floid_stainberg_2-'+imgname,newimg2)

    print("Resultados salvos em:")
    print('resultados/floid_stainberg/floid_stainberg_1-'+imgname)
    print('resultados/floid_stainberg/floid_stainberg_2-'+imgname)

    cv.waitKey(0)
    cv.destroyAllWindows()
    
except:
    print("Erro")