import cv2 as cv
import numpy as np
import sys
import time
import os, math

def L(n,img,x,y,dx):
    L1 = ((-1)*dx*(dx-1)*(dx-2)*img[y+n-2][x-1])/6
    L2 = ((dx+1)*(dx-1)*(dx-2)*img[y+n-2][x])/2
    L3 = ((-1)*dx*(dx+1)*(dx-2)*img[y+n-2][x+1])/2
    L4 = (dx*(dx+1)*(dx-1)*img[y+n-2][x+2])/6

    return L1+L2+L3+L4

def polinomios_lagrange(img,x,y):
    dx = x - math.trunc(x)
    dy = y - math.trunc(y)

    x = math.trunc(x) 
    y = math.trunc(y)

    P1 = ((-1)*dy*(dy-1)*(dy-2)*L(1,img,x,y,dx))/6
    P2 = ((dy+1)*(dy-1)*(dy-2)*L(2,img,x,y,dx))/2
    P3 = ((-1)*dy*(dy+1)*(dy-2)*L(3,img,x,y,dx))/2
    P4 = (dy*(dy+1)*(dy-1)*L(4,img,x,y,dx))/6

    return P1+P2+P3+P4

def R(s):
    return (((P(s+2)**3) - 4*(P(s+1)**3) + 6*(P(s)**3) - 4*(P(s-1)**3))/6)

def P(t):
    if t > 0:
        return t
    else:
        return 0

def bicubica(img,x,y):
    dx = x - math.trunc(x)
    dy = y - math.trunc(y)

    x = math.trunc(x) 
    y = math.trunc(y)

    soma = 0

    for m in range(-1,3):
        for n in range(-1,3):
            soma = soma + img[y+n][x+m]*R(m-dx)*R(dy-n)
    
    return soma

def bilinear(img,x,y):
    dx = x - math.trunc(x)
    dy = y - math.trunc(y)

    x = math.trunc(x) 
    y = math.trunc(y)

    return (1-dx)*(1-dy)*img[y][x] + dx*(1-dy)*img[y][x+1] + (1-dx)*dy*img[y+1][x] + dx*dy*img[y+1][x+1]

def rotacionar(img,angulo,interpolacao):
    rad = angulo*math.pi/180
    print("Rotacao de",angulo,"graus utilizando o metodo metodo de interpolacao por ",end="")

    dim = img.shape

    alt = dim[0]
    larg = dim[1]
    prof = dim[2]

    newimg = np.zeros((alt,larg,prof),np.uint8)

    y1 = alt/2
    x1 = larg/2

    cosseno = math.cos(rad)
    seno = math.sin(rad)
    if interpolacao == "vmp":
        print("Vizinho mais proximo")
        for i in range(len(newimg)):
            for j in range(len(newimg[i])):
                x = round(j*cosseno - i*seno + x1*(1-cosseno) + y1*seno)
                y = round(j*seno + i*cosseno + y1*(1-cosseno) - x1*seno)

                if x >= larg or y >= alt or x < 0 or y < 0:
                    newimg[i][j][:] = 255
                else:
                    newimg[i][j] = img[y][x]
                   
    elif interpolacao == "bl":
        print("Bilinear")
        for i in range(len(newimg)):
            for j in range(len(newimg[i])):
                x = j*cosseno - i*seno + x1*(1-cosseno) + y1*seno
                y = j*seno + i*cosseno + y1*(1-cosseno) - x1*seno

                if x >= (larg - 1) or y >= (alt - 1) or x < 0 or y < 0:
                    newimg[i][j][:] = 255
                else:
                    newimg[i][j][:] = bilinear(img,x,y)
    elif interpolacao == "bc":
        print("Bicubica")
        for i in range(len(newimg)):
            for j in range(len(newimg[i])):
                x = j*cosseno - i*seno + x1*(1-cosseno) + y1*seno
                y = j*seno + i*cosseno + y1*(1-cosseno) - x1*seno

                if x >= (larg - 2) or y >= (alt - 2) or x < 1 or y < 1:
                    newimg[i][j][:] = 255
                else:
                    newimg[i][j][:] = bicubica(img,x,y)
    elif interpolacao == "pl":
        print("Polinomios de Lagrange")
        for i in range(len(newimg)):
            for j in range(len(newimg[i])):
                x = j*cosseno - i*seno + x1*(1-cosseno) + y1*seno
                y = j*seno + i*cosseno + y1*(1-cosseno) - x1*seno

                if x >= (larg - 2) or y >= (alt - 2) or x < 1 or y < 1:
                    newimg[i][j][:] = 255
                else:
                    newimg[i][j][:] = polinomios_lagrange(img,x,y)
    else:
        print("Metodo de interpolacao nao reconhecido.")
        print("vpm == Vizinho Mais Proximo")
        print("bl == Bilinear")
        print("bc == Bicubica")
        print("pl == Polinomios de Lagrange")


    return newimg

def escala(img,Sx,Sy,interpolacao):

    dim = img.shape

    alt = int(dim[0]*Sy)
    larg = int(dim[1]*Sx)
    prof = dim[2]

    newimg = np.zeros((alt,larg,prof),np.uint8)

    if interpolacao == "vmp":
        print("Vizinho mais proximo")
        for i in range(alt-1):
            for j in range(larg-1):
                x = round(j/Sx)
                y = round(i/Sy)

                newimg[i][j] = img[y][x]
                   
    elif interpolacao == "bl":
        print("Bilinear")
        for i in range(alt-2):
            for j in range(larg-2):
                x = j/Sx
                y = i/Sy

                newimg[i][j][:] = bilinear(img,x,y)
    elif interpolacao == "bc":
        print("Bicubica")
        for i in range(alt-4):
            for j in range(larg-4):
                x = j/Sx
                y = i/Sy

                newimg[i][j][:] = bicubica(img,x,y)
    elif interpolacao == "pl":
        print("Polinomios de Lagrange")
        for i in range(alt-4):
            for j in range(larg-4):
                x = j/Sx
                y = i/Sy

                newimg[i][j][:] = polinomios_lagrange(img,x,y)
    else:
        print("Metodo de interpolacao nao reconhecido.")
        print("vpm == Vizinho Mais Proximo")
        print("bl == Bilinear")
        print("bc == Bicubica")
        print("pl == Polinomios de Lagrange")


    return newimg
