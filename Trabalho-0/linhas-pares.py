import cv2 as cv
import numpy as np
import sys

imgname = sys.argv[1]
imgpath = "img/" + imgname

try:
    img = cv.imread(imgpath)

    newimg = img.copy()
    newimg[::2] = np.flip(img[::2], axis = 1)        # Linhas pares invertidas no eixo horizontal

    respath = "resultados/pares-invertidas/pares-invertidas-" + imgname
    cv.imwrite(respath,newimg)

    print("Resultado salvo em:",respath)

    cv.imshow("Original",img)
    cv.imshow("Linhas pares invertidas",newimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")
