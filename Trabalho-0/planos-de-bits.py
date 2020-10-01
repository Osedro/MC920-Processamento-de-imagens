import cv2 as cv
import numpy as np
import sys

imgname = sys.argv[1]
imgpath = "img/" + imgname

try:

    img = cv.imread(imgpath)
    cv.imshow("Original",img) 

    for bit in range(8):
        newimg = (((img/(2**bit))%2)*255).astype(np.uint8)      # Extração do plano de bits

        respath = "resultados/planos-de-bits/bit-" + str(bit)+ "-" + imgname
        cv.imwrite(respath,newimg)
        
        print("Resultado salvo em:",respath)
        
        cv.imshow("Plano de bit " + str(bit),newimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")