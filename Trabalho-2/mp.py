import multiprocessing as mp
import cv2 as cv
import numpy as np
import sys
import os
from meio_tom_lib import *

def sir1(img):
    res = sierra_1(img)*255
    cv.imshow("Sierra metodo 1",res)
    cv.waitKey(0)
    cv.destroyAllWindows()

def sir2(img):
    res = sierra_2(img)*255
    cv.imshow("Sierra metodo 2",res)
    cv.waitKey(0)
    cv.destroyAllWindows()

imgname = sys.argv[1]
imgpath = "img/" + imgname

try:
    img1 = cv.imread(imgpath)
    img2 = cv.imread(imgpath)

    process_1 = mp.Process(target = sir1, args = (img1,))
    process_2 = mp.Process(target = sir2, args = (img2,))

    process_3 = mp.Process(target = sir1, args = (img1,))
    process_4 = mp.Process(target = sir2, args = (img2,))

    process_5 = mp.Process(target = sir1, args = (img1,))
    process_6 = mp.Process(target = sir2, args = (img2,))

    process_7 = mp.Process(target = sir1, args = (img1,))
    process_8 = mp.Process(target = sir2, args = (img2,))

    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()
    process_5.start()
    process_6.start()
    process_7.start()
    process_8.start()

    process_1.join()
    process_2.join()
    process_3.join()
    process_4.join()
    process_5.join()
    process_6.join()
    process_7.join()
    process_8.join()

    print(len(os.sched_getaffinity(0)))
except:
    print("ERRO")