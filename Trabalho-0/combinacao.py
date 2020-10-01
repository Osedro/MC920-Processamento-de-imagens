import cv2 as cv
import numpy as np
import sys

imgnameA = sys.argv[1]
imgnameB = sys.argv[2]

imgpathA = "img/" + imgnameA
imgpathB = "img/" + imgnameB

peso = float(sys.argv[3])

if peso > 1 or peso < 0:
    print("Valor de peso fora do intervalo [0,1]")
else:
    try:    
        imgA = cv.imread(imgpathA)
        imgB = cv.imread(imgpathB)

        cv.imshow("Imagem A",imgA)   
        cv.imshow("Imagem B",imgB) 

        newimg1 = (peso*imgA+(1-peso)*imgB).astype(np.uint8) 
        cv.imshow("Peso " + str(peso),newimg1)

        respath = "resultados/combinacoes/combinacao-"+ str(peso) + "-" + imgnameA.split(".")[0] + "-" + imgnameB
        cv.imwrite(respath,newimg1)

        print("Resultado salvo em:",respath)

        cv.waitKey(0)
        cv.destroyAllWindows()
    except:
        print("Imagens " + imgnameA + " e " + imgnameB + " nao encontradas")