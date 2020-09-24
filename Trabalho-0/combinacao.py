import cv2 as cv
import numpy as np

imgpathA = "img/baboon.png"
imgpathB = "img/city.png"
imgA = cv.imread(imgpathA)
imgB = cv.imread(imgpathB)
try:    
    cv.imshow("Imagem A",imgA)   
    cv.imshow("Imagem B",imgB) 

    razao = 0.25
    newimg1 = (razao*imgA+(1-razao)*imgB).astype(np.uint8) 
    cv.imshow("Razao " + str(razao),newimg1)
    cv.imwrite("resultados/baboon+city-"+str(razao)+".png",newimg1)

    razao = 0.50
    newimg2 = (razao*imgA+(1-razao)*imgB).astype(np.uint8) 
    cv.imshow("Razao " + str(razao),newimg2)
    cv.imwrite("resultados/baboon+city-"+str(razao)+".png",newimg2)

    razao = 0.75
    newimg3 = (razao*imgA+(1-razao)*imgB).astype(np.uint8) 
    cv.imshow("Razao " + str(razao),newimg3)
    cv.imwrite("resultados/baboon+city-"+str(razao)+".png",newimg3)

    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagens nao encontradas")