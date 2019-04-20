import cv2
import numpy as np
import os
import statistics
import sys
np.set_printoptions(threshold=sys.maxsize)


def ReturnValue(img):
    orginal_pixels = np.array(cv2.imread(os.path.join(os.path.dirname(__file__), 'Arena_Imgs','arena1.png'),0))
    dectecting_img = np.subtract(img, orginal_pixels)
    return dectecting_img

def DetectChange(img):
    orginal_pixels = np.array(cv2.imread(os.path.join(os.path.dirname(__file__), 'Arena_Imgs','arena1.png'),0))
    dectecting_img = np.subtract(img, orginal_pixels)
    change = np.count_nonzero(dectecting_img)
    return change


def GetLocationOfChange(img):
    orginal_pixels = np.array(cv2.imread(os.path.join(os.path.dirname(__file__), 'Arena_Imgs','arena1.png'),0))
    dectecting_img = np.subtract(img, orginal_pixels)
    locations = np.nonzero(dectecting_img)
    row = locations[0] #y
    column = locations[1]#x
    points = np.column_stack((column,row))

    return np.median(points,axis=0)
