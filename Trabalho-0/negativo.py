import cv2 as cv
import numpy as np

imgpath = "img/baboon.png"
try:
    img = cv.imread(imgpath)

    negimg = (255-img).astype(np.uint8)    # Negativo

    cv.imwrite("resultados/baboon-negativo.png",negimg)

    cv.imshow("Original",img)
    cv.imshow("Negativa",negimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")
