import cv2 as cv
import numpy as np

def floid_stainberg_1(img):

    f = img.copy()
    g = np.zeros(f.shape)

    for y in range(len(f)):
        print("Processando pelo metodo 1:",format(100*y/len(f),'.2f'),"%")
        for x in range(len(f[y])):
            for c in range(len(f[y][x])):

                if f[y][x][c] < 128:
                    g[y][x][c] = 0
                else:
                    g[y][x][c] = 1

                erro = f[y][x][c] - g[y][x][c]*255

                try:
                    f[y][x+1][c] = f[y][x+1][c] + erro*(7/16)
                except:
                    pass

                try:
                    f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(3/16)
                except:
                    pass
                
                try:
                    f[y+1][x][c] = f[y+1][x][c] + erro*(5/16)
                except:
                    pass

                try:
                    f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(1/16)
                except:
                    pass


    return g

def floid_stainberg_2(img):

    f = img.copy()
    g = np.zeros(f.shape)

    for y in range(len(f)):
        print("Processando pelo metodo 2:",format(100*y/len(f),'.2f'),"%")
        if y%2 == 0:
            for x in range(len(f[y])):
                for c in range(len(f[y][x])):

                    if f[y][x][c] < 128:
                        g[y][x][c] = 0
                    else:
                        g[y][x][c] = 1

                    erro = f[y][x][c] - g[y][x][c]*255

                    try:
                        f[y][x+1][c] = f[y][x+1][c] + erro*(7/16)
                    except:
                        pass

                    try:
                        f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(3/16)
                    except:
                        pass
                    
                    try:
                        f[y+1][x][c] = f[y+1][x][c] + erro*(5/16)
                    except:
                        pass

                    try:
                        f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(1/16)
                    except:
                        pass
        
        else:
            for x in range(len(f[y])-1,-1,-1):
                for c in range(len(f[y][x])):

                    if f[y][x][c] < 128:
                        g[y][x][c] = 0
                    else:
                        g[y][x][c] = 1

                    erro = f[y][x][c] - g[y][x][c]*255

                    try:
                        f[y][x-1][c] = f[y][x-1][c] + erro*(7/16)
                    except:
                        pass

                    try:
                        f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(3/16)
                    except:
                        pass
                    
                    try:
                        f[y+1][x][c] = f[y+1][x][c] + erro*(5/16)
                    except:
                        pass

                    try:
                        f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(1/16)
                    except:
                        pass

    return g

def stevenson_arce_1(img):
    f = img.copy()
    g = np.zeros(f.shape)

    for y in range(len(f)):
        print("Processando pelo metodo 1:",format(100*y/len(f),'.2f'),"%")
        for x in range(len(f[y])):
            for c in range(len(f[y][x])):

                if f[y][x][c] < 128:
                    g[y][x][c] = 0
                else:
                    g[y][x][c] = 1

                erro = f[y][x][c] - g[y][x][c]*255

                try:
                    f[y][x+2][c] = f[y][x+2][c] + erro*(32/200)
                except:
                    pass

                try:
                    f[y+1][x-3][c] = f[y+1][x-3][c] + erro*(12/200)
                except:
                    pass

                try:
                    f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(26/200)
                except:
                    pass

                try:
                    f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(30/200)
                except:
                    pass

                try:
                    f[y+1][x+3][c] = f[y+1][x+3][c] + erro*(16/200)
                except:
                    pass

                try:
                    f[y+2][x-2][c] = f[y+2][x-2][c] + erro*(12/200)
                except:
                    pass

                try:
                    f[y+2][x][c] = f[y+2][x][c] + erro*(26/200)
                except:
                    pass

                try:
                    f[y+2][x+2][c] = f[y+2][x+2][c] + erro*(12/200)
                except:
                    pass

                try:
                    f[y+3][x-3][c] = f[y+3][x-3][c] + erro*(5/200)
                except:
                    pass

                try:
                    f[y+3][x-1][c] = f[y+3][x-1][c] + erro*(12/200)
                except:
                    pass

                try:
                    f[y+3][x+1][c] = f[y+3][x+1][c] + erro*(12/200)
                except:
                    pass

                try:
                    f[y+3][x+3][c] = f[y+3][x+3][c] + erro*(5/200)
                except:
                    pass


    return g

def stevenson_arce_2(img):
    f = img.copy()
    g = np.zeros(f.shape)

    for y in range(len(f)):
        print("Processando pelo metodo 2:",format(100*y/len(f),'.2f'),"%")
        if y%2 == 0:
            for x in range(len(f[y])):
                for c in range(len(f[y][x])):

                    if f[y][x][c] < 128:
                        g[y][x][c] = 0
                    else:
                        g[y][x][c] = 1

                    erro = f[y][x][c] - g[y][x][c]*255

                    try:
                        f[y][x+2][c] = f[y][x+2][c] + erro*(32/200)
                    except:
                        pass

                    try:
                        f[y+1][x-3][c] = f[y+1][x-3][c] + erro*(12/200)
                    except:
                        pass

                    try:
                        f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(26/200)
                    except:
                        pass

                    try:
                        f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(30/200)
                    except:
                        pass

                    try:
                        f[y+1][x+3][c] = f[y+1][x+3][c] + erro*(16/200)
                    except:
                        pass

                    try:
                        f[y+2][x-2][c] = f[y+2][x-2][c] + erro*(12/200)
                    except:
                        pass

                    try:
                        f[y+2][x][c] = f[y+2][x][c] + erro*(26/200)
                    except:
                        pass

                    try:
                        f[y+2][x+2][c] = f[y+2][x+2][c] + erro*(12/200)
                    except:
                        pass

                    try:
                        f[y+3][x-3][c] = f[y+3][x-3][c] + erro*(5/200)
                    except:
                        pass

                    try:
                        f[y+3][x-1][c] = f[y+3][x-1][c] + erro*(12/200)
                    except:
                        pass

                    try:
                        f[y+3][x+1][c] = f[y+3][x+1][c] + erro*(12/200)
                    except:
                        pass

                    try:
                        f[y+3][x+3][c] = f[y+3][x+3][c] + erro*(5/200)
                    except:
                        pass
        else:
            for x in range(len(f[y])-1,-1,-1):
                for c in range(len(f[y][x])):

                    if f[y][x][c] < 128:
                        g[y][x][c] = 0
                    else:
                        g[y][x][c] = 1

                    erro = f[y][x][c] - g[y][x][c]*255

                    try:
                        f[y][x-2][c] = f[y][x-2][c] + erro*(32/200)
                    except:
                        pass

                    try:
                        f[y+1][x+3][c] = f[y+1][x+3][c] + erro*(12/200)
                    except:
                        pass

                    try:
                        f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(26/200)
                    except:
                        pass

                    try:
                        f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(30/200)
                    except:
                        pass

                    try:
                        f[y+1][x-3][c] = f[y+1][x-3][c] + erro*(16/200)
                    except:
                        pass

                    try:
                        f[y+2][x+2][c] = f[y+2][x+2][c] + erro*(12/200)
                    except:
                        pass

                    try:
                        f[y+2][x][c] = f[y+2][x][c] + erro*(26/200)
                    except:
                        pass

                    try:
                        f[y+2][x-2][c] = f[y+2][x-2][c] + erro*(12/200)
                    except:
                        pass

                    try:
                        f[y+3][x+3][c] = f[y+3][x+3][c] + erro*(5/200)
                    except:
                        pass

                    try:
                        f[y+3][x+1][c] = f[y+3][x+1][c] + erro*(12/200)
                    except:
                        pass

                    try:
                        f[y+3][x-1][c] = f[y+3][x-1][c] + erro*(12/200)
                    except:
                        pass

                    try:
                        f[y+3][x-3][c] = f[y+3][x-3][c] + erro*(5/200)
                    except:
                        pass


    return g

def burkes_1(img):
    f = img.copy()
    g = np.zeros(f.shape)

    for y in range(len(f)):
        print("Processando pelo metodo 1:",format(100*y/len(f),'.2f'),"%")
        for x in range(len(f[y])):
            for c in range(len(f[y][x])):

                if f[y][x][c] < 128:
                    g[y][x][c] = 0
                else:
                    g[y][x][c] = 1

                erro = f[y][x][c] - g[y][x][c]*255
                
                try:
                    f[y][x+1][c] = f[y][x+1][c] + erro*(8/32)
                except:
                    pass

                try:
                    f[y][x+2][c] = f[y][x+2][c] + erro*(4/32)
                except:
                    pass

                try:
                    f[y+1][x-2][c] = f[y+1][x-2][c] + erro*(2/32)
                except:
                    pass

                try:
                    f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(4/32)
                except:
                    pass

                try:
                    f[y+1][x][c] = f[y+1][x][c] + erro*(8/32)
                except:
                    pass

                try:
                    f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(4/32)
                except:
                    pass

                try:
                    f[y+1][x+2][c] = f[y+1][x+2][c] + erro*(2/32)
                except:
                    pass

    return g

def burkes_2(img):
    f = img.copy()
    g = np.zeros(f.shape)

    for y in range(len(f)):
        print("Processando pelo metodo 2:",format(100*y/len(f),'.2f'),"%")
        if y%2 == 0:
            for x in range(len(f[y])):
                for c in range(len(f[y][x])):

                    if f[y][x][c] < 128:
                        g[y][x][c] = 0
                    else:
                        g[y][x][c] = 1

                    erro = f[y][x][c] - g[y][x][c]*255
                    
                    try:
                        f[y][x+1][c] = f[y][x+1][c] + erro*(8/32)
                    except:
                        pass

                    try:
                        f[y][x+2][c] = f[y][x+2][c] + erro*(4/32)
                    except:
                        pass

                    try:
                        f[y+1][x-2][c] = f[y+1][x-2][c] + erro*(2/32)
                    except:
                        pass

                    try:
                        f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(4/32)
                    except:
                        pass

                    try:
                        f[y+1][x][c] = f[y+1][x][c] + erro*(8/32)
                    except:
                        pass

                    try:
                        f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(4/32)
                    except:
                        pass

                    try:
                        f[y+1][x+2][c] = f[y+1][x+2][c] + erro*(2/32)
                    except:
                        pass
        else:
            for x in range(len(f[y])-1,-1,-1):
                for c in range(len(f[y][x])):

                    if f[y][x][c] < 128:
                        g[y][x][c] = 0
                    else:
                        g[y][x][c] = 1

                    erro = f[y][x][c] - g[y][x][c]*255
                    
                    try:
                        f[y][x-1][c] = f[y][x-1][c] + erro*(8/32)
                    except:
                        pass

                    try:
                        f[y][x-2][c] = f[y][x-2][c] + erro*(4/32)
                    except:
                        pass

                    try:
                        f[y+1][x-2][c] = f[y+1][x-2][c] + erro*(2/32)
                    except:
                        pass

                    try:
                        f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(4/32)
                    except:
                        pass

                    try:
                        f[y+1][x][c] = f[y+1][x][c] + erro*(8/32)
                    except:
                        pass

                    try:
                        f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(4/32)
                    except:
                        pass

                    try:
                        f[y+1][x+2][c] = f[y+1][x+2][c] + erro*(2/32)
                    except:
                        pass


    return g

def sierra_1(img):
    f = img.copy()
    g = np.zeros(f.shape)

    for y in range(len(f)):
        print("Processando pelo metodo 1:",format(100*y/len(f),'.2f'),"%")
        for x in range(len(f[y])):
            for c in range(len(f[y][x])):

                if f[y][x][c] < 128:
                    g[y][x][c] = 0
                else:
                    g[y][x][c] = 1

                erro = f[y][x][c] - g[y][x][c]*255
                
                try:
                    f[y][x+1][c] = f[y][x+1][c] + erro*(5/32)
                except:
                    pass

                try:
                    f[y][x+2][c] = f[y][x+2][c] + erro*(3/32)
                except:
                    pass

                try:
                    f[y+1][x-2][c] = f[y+1][x-2][c] + erro*(2/32)
                except:
                    pass

                try:
                    f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(4/32)
                except:
                    pass

                try:
                    f[y+1][x][c] = f[y+1][x][c] + erro*(5/32)
                except:
                    pass

                try:
                    f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(4/32)
                except:
                    pass

                try:
                    f[y+1][x+2][c] = f[y+1][x+2][c] + erro*(2/32)
                except:
                    pass

                try:
                    f[y+2][x-1][c] = f[y+2][x-1][c] + erro*(2/32)
                except:
                    pass

                try:
                    f[y+2][x][c] = f[y+2][x][c] + erro*(3/32)
                except:
                    pass

                try:
                    f[y+2][x+1][c] = f[y+2][x+1][c] + erro*(2/32)
                except:
                    pass

    return g

def sierra_2(img):
    f = img.copy()
    g = np.zeros(f.shape)

    for y in range(len(f)):
        print("Processando pelo metodo 2:",format(100*y/len(f),'.2f'),"%")
        if y%2 == 0:
            for x in range(len(f[y])):
                for c in range(len(f[y][x])):

                    if f[y][x][c] < 128:
                        g[y][x][c] = 0
                    else:
                        g[y][x][c] = 1

                    erro = f[y][x][c] - g[y][x][c]*255
                    
                    try:
                        f[y][x+1][c] = f[y][x+1][c] + erro*(5/32)
                    except:
                        pass

                    try:
                        f[y][x+2][c] = f[y][x+2][c] + erro*(3/32)
                    except:
                        pass

                    try:
                        f[y+1][x-2][c] = f[y+1][x-2][c] + erro*(2/32)
                    except:
                        pass

                    try:
                        f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(4/32)
                    except:
                        pass

                    try:
                        f[y+1][x][c] = f[y+1][x][c] + erro*(5/32)
                    except:
                        pass

                    try:
                        f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(4/32)
                    except:
                        pass

                    try:
                        f[y+1][x+2][c] = f[y+1][x+2][c] + erro*(2/32)
                    except:
                        pass

                    try:
                        f[y+2][x-1][c] = f[y+2][x-1][c] + erro*(2/32)
                    except:
                        pass

                    try:
                        f[y+2][x][c] = f[y+2][x][c] + erro*(3/32)
                    except:
                        pass

                    try:
                        f[y+2][x+1][c] = f[y+2][x+1][c] + erro*(2/32)
                    except:
                        pass
        else:
            for x in range(len(f[y])-1,-1,-1):
                for c in range(len(f[y][x])):

                    if f[y][x][c] < 128:
                        g[y][x][c] = 0
                    else:
                        g[y][x][c] = 1

                    erro = f[y][x][c] - g[y][x][c]*255
                    
                    try:
                        f[y][x-1][c] = f[y][x-1][c] + erro*(5/32)
                    except:
                        pass

                    try:
                        f[y][x-2][c] = f[y][x-2][c] + erro*(3/32)
                    except:
                        pass

                    try:
                        f[y+1][x-2][c] = f[y+1][x-2][c] + erro*(2/32)
                    except:
                        pass

                    try:
                        f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(4/32)
                    except:
                        pass

                    try:
                        f[y+1][x][c] = f[y+1][x][c] + erro*(5/32)
                    except:
                        pass

                    try:
                        f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(4/32)
                    except:
                        pass

                    try:
                        f[y+1][x+2][c] = f[y+1][x+2][c] + erro*(2/32)
                    except:
                        pass

                    try:
                        f[y+2][x-1][c] = f[y+2][x-1][c] + erro*(2/32)
                    except:
                        pass

                    try:
                        f[y+2][x][c] = f[y+2][x][c] + erro*(3/32)
                    except:
                        pass

                    try:
                        f[y+2][x+1][c] = f[y+2][x+1][c] + erro*(2/32)
                    except:
                        pass

    return g

def stucki_1(img):
    f = img.copy()
    g = np.zeros(f.shape)

    for y in range(len(f)):
        print("Processando pelo metodo 1:",format(100*y/len(f),'.2f'),"%")
        for x in range(len(f[y])):
            for c in range(len(f[y][x])):

                if f[y][x][c] < 128:
                    g[y][x][c] = 0
                else:
                    g[y][x][c] = 1

                erro = f[y][x][c] - g[y][x][c]*255
                
                try:
                    f[y][x+1][c] = f[y][x+1][c] + erro*(8/42)
                except:
                    pass

                try:
                    f[y][x+2][c] = f[y][x+2][c] + erro*(4/42)
                except:
                    pass

                try:
                    f[y+1][x-2][c] = f[y+1][x-2][c] + erro*(2/42)
                except:
                    pass

                try:
                    f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(4/42)
                except:
                    pass

                try:
                    f[y+1][x][c] = f[y+1][x][c] + erro*(8/42)
                except:
                    pass

                try:
                    f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(4/42)
                except:
                    pass

                try:
                    f[y+1][x+2][c] = f[y+1][x+2][c] + erro*(2/42)
                except:
                    pass

                try:
                    f[y+2][x-2][c] = f[y+2][x-2][c] + erro*(1/42)
                except:
                    pass

                try:
                    f[y+2][x-1][c] = f[y+2][x-1][c] + erro*(2/42)
                except:
                    pass

                try:
                    f[y+2][x][c] = f[y+2][x][c] + erro*(4/42)
                except:
                    pass

                try:
                    f[y+2][x+1][c] = f[y+2][x+1][c] + erro*(2/42)
                except:
                    pass

                try:
                    f[y+2][x+2][c] = f[y+2][x+2][c] + erro*(1/42)
                except:
                    pass

    return g

def stucki_2(img):
    f = img.copy()
    g = np.zeros(f.shape)

    for y in range(len(f)):
        print("Processando pelo metodo 2:",format(100*y/len(f),'.2f'),"%")
        if y%2 == 0:
            for x in range(len(f[y])):
                for c in range(len(f[y][x])):

                    if f[y][x][c] < 128:
                        g[y][x][c] = 0
                    else:
                        g[y][x][c] = 1

                    erro = f[y][x][c] - g[y][x][c]*255
                    
                    try:
                        f[y][x+1][c] = f[y][x+1][c] + erro*(8/42)
                    except:
                        pass

                    try:
                        f[y][x+2][c] = f[y][x+2][c] + erro*(4/42)
                    except:
                        pass

                    try:
                        f[y+1][x-2][c] = f[y+1][x-2][c] + erro*(2/42)
                    except:
                        pass

                    try:
                        f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(4/42)
                    except:
                        pass

                    try:
                        f[y+1][x][c] = f[y+1][x][c] + erro*(8/42)
                    except:
                        pass

                    try:
                        f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(4/42)
                    except:
                        pass

                    try:
                        f[y+1][x+2][c] = f[y+1][x+2][c] + erro*(2/42)
                    except:
                        pass

                    try:
                        f[y+2][x-2][c] = f[y+2][x-2][c] + erro*(1/42)
                    except:
                        pass

                    try:
                        f[y+2][x-1][c] = f[y+2][x-1][c] + erro*(2/42)
                    except:
                        pass

                    try:
                        f[y+2][x][c] = f[y+2][x][c] + erro*(4/42)
                    except:
                        pass

                    try:
                        f[y+2][x+1][c] = f[y+2][x+1][c] + erro*(2/42)
                    except:
                        pass

                    try:
                        f[y+2][x+2][c] = f[y+2][x+2][c] + erro*(1/42)
                    except:
                        pass

        else:
            for x in range(len(f[y])-1,-1,-1):
                for c in range(len(f[y][x])):

                    if f[y][x][c] < 128:
                        g[y][x][c] = 0
                    else:
                        g[y][x][c] = 1

                    erro = f[y][x][c] - g[y][x][c]*255
                    
                    try:
                        f[y][x-1][c] = f[y][x-1][c] + erro*(8/42)
                    except:
                        pass

                    try:
                        f[y][x-2][c] = f[y][x-2][c] + erro*(4/42)
                    except:
                        pass

                    try:
                        f[y+1][x-2][c] = f[y+1][x-2][c] + erro*(2/42)
                    except:
                        pass

                    try:
                        f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(4/42)
                    except:
                        pass

                    try:
                        f[y+1][x][c] = f[y+1][x][c] + erro*(8/42)
                    except:
                        pass

                    try:
                        f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(4/42)
                    except:
                        pass

                    try:
                        f[y+1][x+2][c] = f[y+1][x+2][c] + erro*(2/42)
                    except:
                        pass

                    try:
                        f[y+2][x-2][c] = f[y+2][x-2][c] + erro*(1/42)
                    except:
                        pass

                    try:
                        f[y+2][x-1][c] = f[y+2][x-1][c] + erro*(2/42)
                    except:
                        pass

                    try:
                        f[y+2][x][c] = f[y+2][x][c] + erro*(4/42)
                    except:
                        pass

                    try:
                        f[y+2][x+1][c] = f[y+2][x+1][c] + erro*(2/42)
                    except:
                        pass

                    try:
                        f[y+2][x+2][c] = f[y+2][x+2][c] + erro*(1/42)
                    except:
                        pass

    return g

def jarvis_judice_ninke_1(img):
    f = img.copy()
    g = np.zeros(f.shape)

    for y in range(len(f)):
        print("Processando pelo metodo 1:",format(100*y/len(f),'.2f'),"%")
        for x in range(len(f[y])):
            for c in range(len(f[y][x])):

                if f[y][x][c] < 128:
                    g[y][x][c] = 0
                else:
                    g[y][x][c] = 1

                erro = f[y][x][c] - g[y][x][c]*255
                
                try:
                    f[y][x+1][c] = f[y][x+1][c] + erro*(7/48)
                except:
                    pass

                try:
                    f[y][x+2][c] = f[y][x+2][c] + erro*(5/48)
                except:
                    pass

                try:
                    f[y+1][x-2][c] = f[y+1][x-2][c] + erro*(3/48)
                except:
                    pass

                try:
                    f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(5/48)
                except:
                    pass

                try:
                    f[y+1][x][c] = f[y+1][x][c] + erro*(7/48)
                except:
                    pass

                try:
                    f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(5/48)
                except:
                    pass

                try:
                    f[y+1][x+2][c] = f[y+1][x+2][c] + erro*(3/48)
                except:
                    pass

                try:
                    f[y+2][x-2][c] = f[y+2][x-2][c] + erro*(1/48)
                except:
                    pass

                try:
                    f[y+2][x-1][c] = f[y+2][x-1][c] + erro*(3/48)
                except:
                    pass

                try:
                    f[y+2][x][c] = f[y+2][x][c] + erro*(5/48)
                except:
                    pass

                try:
                    f[y+2][x+1][c] = f[y+2][x+1][c] + erro*(3/48)
                except:
                    pass

                try:
                    f[y+2][x+2][c] = f[y+2][x+2][c] + erro*(1/48)
                except:
                    pass

    return g

def jarvis_judice_ninke_2(img):
    f = img.copy()
    g = np.zeros(f.shape)

    for y in range(len(f)):
        print("Processando pelo metodo 2:",format(100*y/len(f),'.2f'),"%")
        if y%2 == 0:
            for x in range(len(f[y])):
                for c in range(len(f[y][x])):

                    if f[y][x][c] < 128:
                        g[y][x][c] = 0
                    else:
                        g[y][x][c] = 1

                    erro = f[y][x][c] - g[y][x][c]*255
                    
                    try:
                        f[y][x+1][c] = f[y][x+1][c] + erro*(7/48)
                    except:
                        pass

                    try:
                        f[y][x+2][c] = f[y][x+2][c] + erro*(5/48)
                    except:
                        pass

                    try:
                        f[y+1][x-2][c] = f[y+1][x-2][c] + erro*(3/48)
                    except:
                        pass

                    try:
                        f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(5/48)
                    except:
                        pass

                    try:
                        f[y+1][x][c] = f[y+1][x][c] + erro*(7/48)
                    except:
                        pass

                    try:
                        f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(5/48)
                    except:
                        pass

                    try:
                        f[y+1][x+2][c] = f[y+1][x+2][c] + erro*(3/48)
                    except:
                        pass

                    try:
                        f[y+2][x-2][c] = f[y+2][x-2][c] + erro*(1/48)
                    except:
                        pass

                    try:
                        f[y+2][x-1][c] = f[y+2][x-1][c] + erro*(3/48)
                    except:
                        pass

                    try:
                        f[y+2][x][c] = f[y+2][x][c] + erro*(5/48)
                    except:
                        pass

                    try:
                        f[y+2][x+1][c] = f[y+2][x+1][c] + erro*(3/48)
                    except:
                        pass

                    try:
                        f[y+2][x+2][c] = f[y+2][x+2][c] + erro*(1/48)
                    except:
                        pass

        else:
            for x in range(len(f[y])-1,-1,-1):
                for c in range(len(f[y][x])):

                    if f[y][x][c] < 128:
                        g[y][x][c] = 0
                    else:
                        g[y][x][c] = 1

                    erro = f[y][x][c] - g[y][x][c]*255
                    
                    try:
                        f[y][x-1][c] = f[y][x-1][c] + erro*(7/48)
                    except:
                        pass

                    try:
                        f[y][x-2][c] = f[y][x-2][c] + erro*(5/48)
                    except:
                        pass

                    try:
                        f[y+1][x-2][c] = f[y+1][x-2][c] + erro*(3/48)
                    except:
                        pass

                    try:
                        f[y+1][x-1][c] = f[y+1][x-1][c] + erro*(5/48)
                    except:
                        pass

                    try:
                        f[y+1][x][c] = f[y+1][x][c] + erro*(7/48)
                    except:
                        pass

                    try:
                        f[y+1][x+1][c] = f[y+1][x+1][c] + erro*(5/48)
                    except:
                        pass

                    try:
                        f[y+1][x+2][c] = f[y+1][x+2][c] + erro*(3/48)
                    except:
                        pass

                    try:
                        f[y+2][x-2][c] = f[y+2][x-2][c] + erro*(1/48)
                    except:
                        pass

                    try:
                        f[y+2][x-1][c] = f[y+2][x-1][c] + erro*(3/48)
                    except:
                        pass

                    try:
                        f[y+2][x][c] = f[y+2][x][c] + erro*(5/48)
                    except:
                        pass

                    try:
                        f[y+2][x+1][c] = f[y+2][x+1][c] + erro*(3/48)
                    except:
                        pass

                    try:
                        f[y+2][x+2][c] = f[y+2][x+2][c] + erro*(1/48)
                    except:
                        pass

    return g
