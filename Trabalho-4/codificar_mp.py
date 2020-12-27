import cv2 as cv
import numpy as np
import sys
import esteganografia_lib as est
import time

if __name__ == '__main__':

    inicio = time.time()
    
    imgname = sys.argv[1]                   # Primeiro argumento: nome e formato da imagem

    msgname = sys.argv[2]                   # Segundo argumento: nome e formato da mensagem

    try:
        plano_bits = int(sys.argv[3])           # Terceiro argumento: plano de bits que a mensagem será codificada
    except:
        plano_bits = 0
        
    if msgname.split(".")[1] == "txt":
        est.codificar_mp_txt(imgname,msgname,plano_bits)
    elif msgname.split(".")[1] == "png":
        est.codificar_png(imgname,msgname,plano_bits)
    else:
        print("Este tipo de arquivo não pode ser codificado :(")
    
    fim = time.time()

    print("Tempo de execucao:",fim - inicio,"s")


