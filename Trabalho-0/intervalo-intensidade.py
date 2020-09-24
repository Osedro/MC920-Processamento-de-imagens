import cv2 as cv
import numpy as np

imgpath = "img/seagull.png"
img = cv.imread(imgpath)
try:
    newimg = np.uint8(100) + ((img/255)*100).astype(np.uint8)     # Intervalo de intensidades convertido para [100,200]

    cv.imwrite("resultados/seagul-intervalo.png",newimg)

    cv.imshow("Original",img)
    cv.imshow("Intervalo de intensidade alterado",newimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")
