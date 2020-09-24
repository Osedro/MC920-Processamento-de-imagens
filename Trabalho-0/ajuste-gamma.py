import cv2 as cv
import numpy as np

imgpath = "img/butterfly.png"
img = cv.imread(imgpath)
try:

    #gamma = float(input())                  # Correção gamma escolhida pelo usuario
    
    # Gamma 1.5
    gamma = 1.5
    aux = img/255
    aux = aux**(1/gamma)
    newimg = (aux*255).astype(np.uint8)     # Correção gamma 

    cv.imwrite("resultados/butterfly-gamma-"+str(gamma)+".png",newimg)

    cv.imshow("Original",img)   
    cv.imshow("Correção gamma " + str(gamma),newimg)
    
    # Gamma 2.5
    gamma = 2.5
    aux = img/255
    aux = aux**(1/gamma)
    newimg = (aux*255).astype(np.uint8)     # Correção gamma 

    cv.imwrite("resultados/butterfly-gamma-"+str(gamma)+".png",newimg)

    cv.imshow("Correção gamma " + str(gamma),newimg)

    # Gamma 3.5
    gamma = 3.5
    aux = img/255
    aux = aux**(1/gamma)
    newimg = (aux*255).astype(np.uint8)     # Correção gamma 

    cv.imwrite("resultados/butterfly-gamma-"+str(gamma)+".png",newimg)

    cv.imshow("Correção gamma " + str(gamma),newimg)
    
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")