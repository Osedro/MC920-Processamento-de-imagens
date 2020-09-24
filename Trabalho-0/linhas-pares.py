import cv2 as cv
import numpy as np

imgpath = "img/city.png"
img = cv.imread(imgpath)
try:
    newimg = img.copy()
    newimg[::2] = np.flip(img[::2], axis = 1)        # Linhas pares invertidas no eixo horizontal

    cv.imwrite("resultados/city-pares-invertidas.png",newimg)

    cv.imshow("Original",img)
    cv.imshow("Linhas pares invertidas",newimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")
