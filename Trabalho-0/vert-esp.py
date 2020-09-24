import cv2 as cv
import numpy as np

imgpath = "img/house.png"
try:
    img = cv.imread(imgpath)

    newimg = np.flip(img,axis=0)       # Espelhamento vertical

    cv.imwrite("resultados/house-espelhada-vertical.png",newimg)

    cv.imshow("Original",img)
    cv.imshow("Espelhada",newimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")
