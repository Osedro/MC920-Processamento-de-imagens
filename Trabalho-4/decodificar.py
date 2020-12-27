import cv2 as cv
import numpy as np
import sys
import esteganografia_lib as est
import time

inicio = time.time()

imgname = sys.argv[1]  
imgpath = "imgs_codificadas/" + imgname

try:
    plano_bits = int(sys.argv[2]) 
except:
    plano_bits = 0

img = cv.imread(imgpath)

altura, largura, bandas = img.shape

imgB = img[:,:,0]           # AZUL  
imgG = img[:,:,1]           # VERDE
imgR = img[:,:,2]           # VERMELHO

planosR = []                # CONTÉM OS PLANOS DE BITS DA BANDA VERMELHA
planosG = []                # CONTÉM OS PLANOS DE BITS DA BANDA VERDE
planosB = []                # CONTÉM OS PLANOS DE BITS DA BANDA AZUL

# SEPARA A IMAGEM EM PLANOS DE BITS PARA CADA BANDA DE COR
for bit in range(8):
    aux = ((imgB/(2**bit))%2).astype(np.uint8)
    planosB.append(aux)

    aux = ((imgG/(2**bit))%2).astype(np.uint8)
    planosG.append(aux)

    aux = ((imgR/(2**bit))%2).astype(np.uint8)
    planosR.append(aux)

tipo = est.get_tipo(planosB,planosG,planosR,plano_bits)

if tipo == "txt":
    est.decodificar_txt(planosB,planosG,planosR,plano_bits,imgname)
elif tipo == "png":
    est.decodificar_png(planosB,planosG,planosR,plano_bits,imgname)
else:
    print("Tipo de mensagem não identificada :(")

fim = time.time()

print("Tempo de execucao:",fim - inicio,"s")