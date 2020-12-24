import cv2 as cv
import numpy as np
import sys

def unir_planos(planos,p):
    altura, largura = planos[0].shape
    saida = np.zeros((altura,largura))
    for i in range(altura):
        for j in range(largura):
            pixel = 0

            for bit in range(8):
                pixel = (pixel + planos[bit][i][j]*(2**bit))

            saida[i][j] = pixel
    
    p.send(saida)
    return

def converte_bits(entrada):
    codificada = entrada.encode("utf-8")
    #codificada = entrada.encode("ansi")
    #print(codificada)
    tam = len(codificada)
    saida = []

    aux = []
    for i in range(32):
        aux.append(int(((tam/(2**i))%2)))
    saida.append(aux)

    
    for c in codificada:
        aux = []
        for i in range(8):
            aux.append(int(((c/(2**i))%2)))
        saida.append(aux)
    return saida