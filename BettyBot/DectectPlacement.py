import cv2
import numpy as np
import os

def ReturnValue(img):
    orginal_pixels = np.array(cv2.imread(os.path.join(os.path.dirname(__file__), 'Arena_Imgs','area1.png'),0))
    dectecting_img = np.subtract(img, orginal_pixels)
    change = np.count_nonzero(dectecting_img)
    return dectecting_img

def DetectChange(img):
    orginal_pixels = np.array(cv2.imread(os.path.join(os.path.dirname(__file__), 'Arena_Imgs','area1.png'),0))
    dectecting_img = np.subtract(img, orginal_pixels)
    change = np.count_nonzero(dectecting_img)
    return change
