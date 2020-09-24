import cv2 as cv
import numpy as np

imgpath = "img/butterfly.png"
img = cv.imread(imgpath)
try:
    newimg = img.copy()

    aux = newimg[0:int(len(newimg)/2)]
    aux = np.flip(aux,axis = 0)
    newimg[int(len(newimg)/2):int(len(newimg))] = aux.astype(np.uint8)       # Espelha as linhas da parte superior para a parte inferior

    cv.imwrite("resultados/butterfly-reflexao.png",newimg)

    cv.imshow("Original",img)   
    cv.imshow("Reflexao no centro",newimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")