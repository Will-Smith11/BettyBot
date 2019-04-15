import cv2
import numpy as np

def firstSlot():
    img = cv2.imread('charaters.png',0)
    aim = np.array(img)
    data = np.array(aim[~np.all(aim == 0, axis=1)])
    data = np.delete(data,[x for x in range(0,121)]+[x for x in range(191,505)],1)
    cv2.imwrite("SkellyArmy.png",data)
    return data

def secondSlot():
    img = cv2.imread('charaters.png',0)
    aim = np.array(img)
    data = np.array(aim[~np.all(aim == 0, axis=1)])
    data = np.delete(data,[x for x in range(0,215)]+[x for x in range(281,505)],1)
    cv2.imwrite("Giant.png",data)
    return data

def thirdSlot():
    img = cv2.imread('charaters.png',0)
    aim = np.array(img)
    data = np.array(aim[~np.all(aim == 0, axis=1)])
    data = np.delete(data,[x for x in range(0,310)]+[x for x in range(376,505)],1)
    cv2.imwrite("Minions.png",data)
    return data

def fourthSlot():
    img = cv2.imread('charaters.png',0)
    aim = np.array(img)
    data = np.array(aim[~np.all(aim == 0, axis=1)])
    data = np.delete(data,[x for x in range(0,405)]+[x for x in range(471,505)],1)
    cv2.imwrite("Fireball.png",data)
    return data

firstSlot()
secondSlot()
thirdSlot()
fourthSlot()

'''
while True:
    cv2.imshow('screen',fourthSlot())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
'''
