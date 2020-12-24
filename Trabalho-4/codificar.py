import cv2 as cv
import numpy as np
import sys
import esteganografia_lib as est
import time

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

# CONVERTE A MENSAGEM EM UMA LISTA DE BYTES, ONDE CADA UM É UMA LISTA DE BITS.
# OS PRIMEIROS BITS SÃO OS MENOS SIGNIFICATIVOS
msgbits = est.converte_bits(msg)

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



plano = 0
linha = 0
coluna = 0

# INSERE A MENSAGEM NO PLANO DE BITS ESCOLHIDO, DIVIDINDO DADOS EM TODAS AS BANDAS
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

# REMONTA A IMAGEM
for i in range(altura):
    for j in range(largura):
        blue = 0
        red = 0
        green = 0
        for bit in range(8):
            blue = (blue + planosB[bit][i][j]*(2**bit))
            green = (green + planosG[bit][i][j]*(2**bit))
            red = (red + planosR[bit][i][j]*(2**bit))


        newimg[i][j][0] = blue
        newimg[i][j][1] = green
        newimg[i][j][2] = red



#cv.imshow("Original",img)
#cv.imshow("Alterada",newimg.astype(np.uint8))

respath = "res/" + textname + "-" + str(plano_bits) + "-" + imgname
cv.imwrite(respath,newimg)

fim = time.time()

print("Tempo de execucao:",fim - inicio,"s")

#cv.waitKey(0)
#cv.destroyAllWindows()

