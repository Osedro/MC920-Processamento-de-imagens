import cv2 as cv
import numpy as np
import sys
from meio_tom_lib import *

#imgname = sys.argv[1]
#imgpath = "img/" + imgname

#filtroindex = int(sys.argv[2])-1

#imgpath = "img/monalisa.png"
imgpath = "/home/leonardo/Documents/MC920/Trabalho-2/img/watch.png"

try:
    img = cv.imread(imgpath)

    newimg1 = stevenson_arce_1(img)*255
    newimg2 = stevenson_arce_2(img)*255

    cv.imshow("Imagem original",img)
    cv.imshow("1",newimg1)
    cv.imshow("2",newimg2)

    #cv.imwrite('/home/leonardo/Documents/MC920/Trabalho-2/resultados/teste.png',newimg1)

    cv.waitKey(0)
    cv.destroyAllWindows()
    
except:
    print("Erro")