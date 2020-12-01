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
    #k = -0.2

    for k1 in range(-10,0,2):
        k = k1/10
        newimg = limi.niblak(img,n,k)*255

        cv.imshow("Imagem Niblak com n = " + str(n) + " e k = " + str(k),newimg)
        cv.waitKey(0)
        cv.destroyAllWindows()

except:
    print("Imagem " + imgname + " não existe na pasta img")

