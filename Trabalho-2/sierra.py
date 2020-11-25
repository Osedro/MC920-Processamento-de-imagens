import cv2 as cv
import numpy as np
import sys
from meio_tom_lib import *

imgname = sys.argv[1]
imgpath = "img/" + imgname


try:
    img = cv.imread(imgpath)

    newimg1 = sierra_1(img)*255
    newimg2 = sierra_2(img)*255

    cv.imshow("Imagem original",img)
    cv.imshow("Sierra metodo 1",newimg1)
    cv.imshow("Sierra metodo 2",newimg2)

    print("")

    cv.imwrite('resultados/sierra/sierra_1-'+imgname,newimg1)
    cv.imwrite('resultados/sierra/sierra_2-'+imgname,newimg2)

    print("Resultados salvos em:")
    print('resultados/sierra/sierra_1-'+imgname)
    print('resultados/sierra/sierra_2-'+imgname)

    cv.waitKey(0)
    cv.destroyAllWindows()
    
except:
    print("Erro")