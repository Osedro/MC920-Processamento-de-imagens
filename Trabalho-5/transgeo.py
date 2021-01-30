import cv2 as cv
import numpy as np
import sys
import time
import os, math
import transgeo_lib as tg

inicio = time.time()

interpolacao = ""
imgname = ""
imgres = ""

rot = False
esc = False

for i in range(1,len(sys.argv)):
    if  sys.argv[i] == "-a":
        i = i + 1
        angulo = float(sys.argv[i])
        rot = True
        
    if  sys.argv[i] == "-e":
        i = i + 1
        escala = float(sys.argv[i])
        esc = True
        esc_type = 0

    if  sys.argv[i] == "-d":
        i = i + 1
        largura_out = int(sys.argv[i])
        i = i + 1
        altura_out = int(sys.argv[i])
        esc = True
        esc_type = 1

    if  sys.argv[i] == "-m":
        i = i + 1
        interpolacao = sys.argv[i]
        '''
        vpm == Vizinho Mais Proximo
        bl == Bilinear
        bc == Bicubica
        pl == Polinomios de Lagrange
        '''

    if  sys.argv[i] == "-i":
        i = i + 1
        imgname = sys.argv[i]

    if  sys.argv[i] == "-o":
        i = i + 1
        imgres = sys.argv[i]

if interpolacao == "":
    interpolacao = "vmp"

if rot == False and esc == False:
    print("Transformacao geometrica nao expecificada")
    exit()

if rot == True and esc == True:
    print("Apenas uma transformacao geometrica e aceita")
    exit()


imgpath = "img/" + imgname

img = cv.imread(imgpath)

if rot == True:
    newimg = tg.rotacionar(img,angulo,interpolacao)
else:
    if esc_type == 0:
        newimg = tg.escala(img,escala,escala,interpolacao)
    else:
        dim = img.shape
        newimg = tg.escala(img,largura_out/dim[1],altura_out/dim[0],interpolacao)
        
cv.imshow("Entrada",img)
cv.imshow("Saida",newimg)

if imgres == "":
    if esc == True and esc_type == 0:
        imgres = "esc_" + str(escala) + "_" + interpolacao + "_" + imgname
    elif esc == True and esc_type == 1:
        imgres = "esc_" + str(altura_out) + "x" + str(largura_out) + "_" + interpolacao + "_" + imgname
    elif rot == True:
        imgres = "rot_" + str(angulo) + "_" + interpolacao + "_" + imgname
    else:
        imgres = "???"
    

respath = "res/" + imgres

cv.imwrite(respath,newimg)

print("Imagem salva em:",respath)

fim = time.time()

print("Tempo de execucao:",fim - inicio,"s")

cv.waitKey(0)
cv.destroyAllWindows()