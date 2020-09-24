import cv2 as cv
import numpy as np

imgpath = "img/city.png"
img = cv.imread(imgpath)

try:
    cv.imshow("Original",img) 

    for bit in range(8):
        newimg = (((img/(2**bit))%2)*255).astype(np.uint8)      # Extração do plano de bits

        cv.imwrite("resultados/city-bit-"+str(bit)+".png",newimg)

        
        cv.imshow("Plane de bit " + str(bit),newimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
except:
    print("Imagem " + imgpath + " não encontrada")