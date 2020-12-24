import cv2 as cv
import numpy as np
import sys
import esteganografia_lib as est
import multiprocessing as mp
import time

if __name__ == '__main__':

    inicio = time.time()

    imgname = sys.argv[1]
    imgpath = "img/" + imgname

    textname = sys.argv[2].split(".")[0]

    plano_bits = int(sys.argv[3])

    arq = open("msg/textos/" + textname + ".txt",'r')
    lines = arq.readlines()
    msg = ""

    for i in lines:
        msg = msg + i
    arq.close()

    msgbits = est.converte_bits(msg)

    img = cv.imread(imgpath)

    altura, largura, bandas = img.shape

    #print(altura*largura*bandas/8)
    #print(len(msgbits)+3)

    imgB = img[:,:,0]           # AZUL  
    imgG = img[:,:,1]           # VERDE
    imgR = img[:,:,2]           # VERMELHO

    planosR = []
    planosG = []
    planosB = []

    for bit in range(8):
        #aux = (((imgB/(2**bit))%2)*255).astype(np.uint8)
        aux = ((imgB/(2**bit))%2).astype(np.uint8)
        planosB.append(aux)

        #aux = (((imgG/(2**bit))%2)*255).astype(np.uint8)
        aux = ((imgG/(2**bit))%2).astype(np.uint8)
        planosG.append(aux)

        #aux = (((imgR/(2**bit))%2)*255).astype(np.uint8)
        aux = ((imgR/(2**bit))%2).astype(np.uint8)
        planosR.append(aux)

    plano = 0
    linha = 0
    coluna = 0

    for i in msgbits:
        for j in i:
            if plano%3 == 0:
                planosB[plano_bits][linha][coluna] = j
            elif plano%3 == 1:
                planosG[plano_bits][linha][coluna] = j
            else:
                planosR[plano_bits][linha][coluna] = j
                coluna = coluna + 1             
            
            plano = plano + 1

            if coluna == largura:
                coluna = 0
                linha = linha + 1
            

    newimg = np.zeros(img.shape)

    parent_connB, child_connB = mp.Pipe()
    parent_connG, child_connG = mp.Pipe()
    parent_connR, child_connR = mp.Pipe()

    p_blue = mp.Process(target = est.unir_planos, args = (planosB,child_connB,))
    p_green = mp.Process(target = est.unir_planos, args = (planosG,child_connG,))
    p_red = mp.Process(target = est.unir_planos, args = (planosR,child_connR,))

    p_blue.start()
    p_green.start()
    p_red.start()

    planoB = parent_connB.recv()
    planoG = parent_connG.recv()
    planoR = parent_connR.recv()

    newimg[:,:,0] = planoB[:,:]
    newimg[:,:,1] = planoG[:,:]
    newimg[:,:,2] = planoR[:,:]

    respath = "res/" + textname + "-" + str(plano_bits) + "-" + imgname

    cv.imwrite(respath,newimg)

    fim = time.time()

    print("Tempo de execucao:",fim - inicio,"s")


