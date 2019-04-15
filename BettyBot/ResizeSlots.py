import cv2
import numpy as np

def firstSlot(img):
    Key = "Z"
    aim = np.array(img)
    data = np.array(aim[~np.all(aim == 0, axis=1)])
    data = np.delete(data,[x for x in range(0,120)]+[x for x in range(191,505)],1)
    return data

def secondSlot(img):
    Key = "X"
    aim = np.array(img)
    data = np.array(aim[~np.all(aim == 0, axis=1)])
    data = np.delete(data,[x for x in range(0,215)]+[x for x in range(286,505)],1)
    return data

def thirdSlot(img):
    Key = "C"
    aim = np.array(img)
    data = np.array(aim[~np.all(aim == 0, axis=1)])
    data = np.delete(data,[x for x in range(0,305)]+[x for x in range(376,505)],1)
    return data

def fourthSlot(img):
    key = "V"
    aim = np.array(img)
    data = np.array(aim[~np.all(aim == 0, axis=1)])
    data = np.delete(data,[x for x in range(0,405)]+[x for x in range(476,505)],1)
    return data

def ElixerSlot(img):
    aim = np.array(img)
    data = np.array(aim[~np.all(aim == 0, axis=1)])
    data = np.delete(data,[x for x in range(0,130)]+[x for x in range(165,505)],1)
    return data
