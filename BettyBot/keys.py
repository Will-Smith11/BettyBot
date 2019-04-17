from pynput.keyboard import Key, Controller
keyboard = Controller()
from pynput.mouse import Button, Controller
mouse = Controller()
import numpy as np
import cv2
import time

def selectCard(slotNum):
    if slotNum == 1:
        keyboard.press('z')
        keyboard.release('z')

    if slotNum == 2:
        keyboard.press('x')
        keyboard.release('x')

    if slotNum == 3:
        keyboard.press('c')
        keyboard.release('c')

    if slotNum == 4:
        keyboard.press('v')
        keyboard.release('v')

def placeMySide(xPos, yPos):
    if not 430 > xPos > 65:
        raise Exception(f"your x Position of: {xPos} is not on the map")

    if not 590 > yPos > 365:
        raise Exception(f"your y Position of: {yPos} is not on the map")

    mouse.position = (xPos, yPos)
    mouse.press(Button.left)
    mouse.release(Button.left)
    return
