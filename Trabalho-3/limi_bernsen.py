import cv2 as cv
import numpy as np
import sys
import limi_lib as limi

imgname = sys.argv[1]

imgpath = "img/" + imgname

try:
    img = cv.imread(imgpath,0)

    cv.imshow("Imagem original",img)

    for n in range(3,51,4):
            
        newimg = limi.bernsen(img,n)*255

        cv.imshow("Imagem com Bernsen e n = "+str(n),newimg)

        cv.waitKey(0)
        cv.destroyAllWindows()
except:
    print("Imagem " + imgname + " não existe na pasta img")

