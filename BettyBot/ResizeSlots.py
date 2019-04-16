import cv2
import numpy as np

def firstSlot(img):
    Key = "Z"
    aim = np.array(img)
    data = np.array(aim[~np.all(aim == 0, axis=1)])
    data = np.delete(data,[x for x in range(0,120)]+[x for x in range(191,505)],1)
    #cv2.imwrite("Minions.png",data)
    return data

def secondSlot(img):
    Key = "X"
    aim = np.array(img)
    data = np.array(aim[~np.all(aim == 0, axis=1)])
    data = np.delete(data,[x for x in range(0,215)]+[x for x in range(286,505)],1)
    #cv2.imwrite("Giant.png",data)
    return data

def thirdSlot(img):
    Key = "C"
    aim = np.array(img)
    data = np.array(aim[~np.all(aim == 0, axis=1)])
    data = np.delete(data,[x for x in range(0,310)]+[x for x in range(381,505)],1)
    #cv2.imwrite("BabyDrag.png",data)
    return data

def fourthSlot(img):
    key = "V"
    aim = np.array(img)
    data = np.array(aim[~np.all(aim == 0, axis=1)])
    data = np.delete(data,[x for x in range(0,405)]+[x for x in range(476,505)],1)
    #cv2.imwrite("Fireball.png",data)
    return data

def ElixerSlot(img):
    aim = np.array(img)
    data = np.array(aim[~np.all(aim == 0, axis=1)])
    data = np.delete(data,[x for x in range(0,130)]+[x for x in range(165,505)],1)
    return data

#firstSlot(cv2.imread("card2.png",0))
#secondSlot(cv2.imread("card2.png",0))
#thirdSlot(cv2.imread("card2.png",0))
#fourthSlot(cv2.imread("card2.png",0))
