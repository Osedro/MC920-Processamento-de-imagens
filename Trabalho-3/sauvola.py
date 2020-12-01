import cv2 as cv
import numpy as np
import sys
import limi_lib as limi

imgname = sys.argv[1]

imgpath = "img/" + imgname


try:
    img = cv.imread(imgpath,0)

    cv.imshow("Imagem original",img)

    n = 15
    k = 0.1
    R = 128

    newimg = limi.sauvola(img,n,k,R)*255


    cv.imshow("Imagem Sauvola com n = " + str(n) + " e k = " + str(k),newimg)
    cv.waitKey(0)
    cv.destroyAllWindows()

except:
    print("Imagem " + imgname + " não existe na pasta img")

