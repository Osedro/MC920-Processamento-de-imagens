import cv2 as cv
import numpy as np
import sys

imgname = sys.argv[1]
imgpath = "img/" + imgname

try:
    img = cv.imread(imgpath)

    newimg = np.uint8(100) + ((img/255)*100).astype(np.uint8)     # Intervalo de intensidades convertido para [100,200]

    respath = "resultados/intervalo-de-intensidades-[100,200]/[100,200]-"+imgname
    cv.imwrite(respath,newimg)

    print("Resultado salvo em:",respath)

    cv.imshow("Original",img)
    cv.imshow("Intervalo de intensidade [100,200]",newimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")
