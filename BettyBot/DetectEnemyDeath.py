import cv2
import numpy as np
from mss import mss
import time


"""
if enemy stops moving he attacks a tower or my card
so he has two states, either he dies or starts moving again

"""


area = np.array([[40,580],[40,355],[455,355],[455,580]],np.int32)

tower1 = np.array([],np.int32)

tower2 = np.array([],np.int32)

kingTower = np.array([],np.int32)


bbox = {'top': 57, 'left': 0, 'width': 420, 'height': 750}
height_percent = 53
width_percent = 60
sct = mss()
last_time = time.time()
pixelChange = 0


def elixerRegion(original_image):
    processed_img = get_towers(areaOfInterest(original_image))
    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2GRAY)
    return processed_img

def areaOfInterest(img):
    #blank mask:
    mask = np.zeros_like(img)
    # fill the mask

    cv2.fillPoly(mask, [area],(255,255,255))
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked

def get_towers(img):
    #cv2.fillPoly(img, [tower1],(0))
    #cv2.fillPoly(img, [kingTower],(0))
    #cv2.fillPoly(img, [tower2],(0))
    return img

#while True:
#def IsEnemyPlaced():
        #get screen img
sct_img = sct.grab(bbox)
#convert img to array
screen = np.array(sct_img)
# resizing the img to fit better on the screen
width = int(screen.shape[1] * width_percent / 100)
height = int(screen.shape[0] * height_percent / 100)
dim = (width, height)
resized = cv2.resize(screen, dim, interpolation = cv2.INTER_AREA)
game_screen = elixerRegion(resized)

while True:
    cv2.imshow('screen', game_screen)
    #print(f'running at {1/(time.time()-last_time)} FPS')
    last_time = time.time()
    # quit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

        # screen shot slots
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite("mySide.png", final_screen)

        #time.sleep(3)
