import cv2 as cv
import numpy as np
import sys
import esteganografia_lib as est
import time

inicio = time.time()

imgname = "hino-0-monalisa.png"
imgpath = "res/" + imgname

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

tammsg = 0

plano = 0
linha = 0
coluna = 0

# ESTRAÇÃO DO TAMANHO DA MENSAGEM, POSICIONADO NOS 4 PRIMEIROS BYTES CODIFICADOS
for i in range(32):
    if plano%3 == 0:
        tammsg = tammsg + (2**i)*planosB[plano_bits][linha][coluna]
    elif plano%3 == 1:
        tammsg = tammsg + (2**i)*planosG[plano_bits][linha][coluna]
    else:
        tammsg = tammsg + (2**i)*planosR[plano_bits][linha][coluna]
        coluna = coluna + 1             
    
    plano = plano + 1

    if coluna == largura:
        coluna = 0
        linha = linha + 1

plano = 0
linha = 0
coluna = 0
modulo = 0
msgbytes = []

for i in range(tammsg+4):
    byte = 0
    for bit in range(8):
        if plano%3 == 0:
            byte = int(byte + (2**bit)*planosB[plano_bits][linha][coluna])
        elif plano%3 == 1:
            byte = int(byte + (2**bit)*planosG[plano_bits][linha][coluna])
        else:
            byte = int(byte + (2**bit)*planosR[plano_bits][linha][coluna])
            coluna = coluna + 1             
        
        plano = plano + 1

        if coluna == largura:
            coluna = 0
            linha = linha + 1
    
    byte = byte.to_bytes(1,'big')
    msgbytes.append(byte)

del(msgbytes[0])
del(msgbytes[0])
del(msgbytes[0])
del(msgbytes[0])
msgbytes = b''.join(msgbytes)

msgfinal = msgbytes.decode("utf-8")

print(msgfinal)

arqname = "msg_enc/" + imgname.split(".")[0] + "-mensagem.txt"

arquivo = open(arqname,'a')

arquivo.write(msgfinal)

arquivo.close()