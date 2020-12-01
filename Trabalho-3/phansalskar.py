import cv2 as cv
import numpy as np
import sys
import limi_lib as limi

imgname = sys.argv[1]

imgpath = "img/" + imgname


try:
    img = cv.imread(imgpath,0)

    cv.imshow("Imagem original",img)

    n = 25
    k = 0.08
    R = 25
    p = 2
    q = 10

    newimg = limi.phansalskar(img,n,k,R,p,q)*255


    cv.imshow("Imagem Phansalskar com n = " + str(n) + " e k = " + str(k),newimg)
    cv.waitKey(0)
    cv.destroyAllWindows()

except:
    print("Imagem " + imgname + " não existe na pasta img")

