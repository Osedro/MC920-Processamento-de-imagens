import cv2 as cv
import numpy as np
import sys

filtros = []

# Realce de bordas
h1 = np.array([[ 0, 0,-1, 0, 0],[ 0,-1,-2,-1, 0],[-1,-2,16,-2,-1],[ 0,-1,-2,-1, 0],[ 0, 0,-1, 0, 0]])

# Filtro de desfoque
h2 = np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]])/256

h3 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

h4 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])

h5 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

h6 = np.ones((3,3))/9

h7 = np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]])

h8 = np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])

h9 = np.identity(9)/9

h10 = np.array([[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,-1],[-1,2,2,2,-1],[-1,-1,-1,-1,-1]])/8

h11 = np.array([[-1,-1,0],[-1,0,1],[0,1,1]])

filtros.append(h1)
filtros.append(h2)
filtros.append(h3)
filtros.append(h4)

filtros.append(h5)
filtros.append(h6)
filtros.append(h7)
filtros.append(h8)

filtros.append(h9)
filtros.append(h10)
filtros.append(h11)