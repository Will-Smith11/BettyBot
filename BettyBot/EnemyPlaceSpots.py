import cv2
import numpy as np
from mss import mss
import time
from DectectPlacement import ReturnValue, DetectChange

area = np.array([[40,330],[40,65],[465,65],[465,330]],np.int32)

tower1 = np.array([[90,195],[90,135],[82,135],[82,110],
                  [156,110],[156,133],[150,133],[150,195]],np.int32)

tower2 = np.array([[355,195],[355,135],[347,135],[347,110],
                  [420,110],[420,133],[414,133],[414,195]],np.int32)

kingTower = np.array([[215,145],[215,65],[290,65],[290,145]],np.int32)


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
    #cv2.fillPoly(mask, [tower1],(255,255,255))
    cv2.fillPoly(mask, [area],(255,255,255))
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked

def get_towers(img):
    cv2.fillPoly(img, [tower1],(0))
    cv2.fillPoly(img, [kingTower],(0))
    cv2.fillPoly(img, [tower2],(0))
    return img


def IsEnemyPlaced():
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

    # divide the saved img and current img to get only objects of the map
    final_screen = ReturnValue(game_screen)
    detectpixel  = DetectChange(game_screen)

    if detectpixel-pixelChange >=2200:
        pixelChange = detectpixel
        return True
    else:
        return False


    '''
    #while True:
    cv2.imshow('screen', final_screen)
    #print(f'running at {1/(time.time()-last_time)} FPS')
    last_time = time.time()
    # quit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
        '''
    # screen shot slots
    #if cv2.waitKey(1) & 0xFF == ord('s'):

        #cv2.imwrite("area1.png", final_screen)

    #time.sleep(3)
