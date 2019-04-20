import numpy as np
import cv2

def box(median_points, img):
    cv2.rectangle(img,(int(median_points[0]-50),int(median_points[1]-50)),
                 (int(median_points[0]+50),int(median_points[1]+50)),(255,0,0),2)
    return img
