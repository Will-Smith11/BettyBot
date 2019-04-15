import numpy as np
from mss import mss
import cv2
import time
import ResizeSlots
from myDeck import check_for_match

#70 X pixel gap
slot1 = np.array([[120,728],[120,670],[190,670],[190,728]],np.int32)
slot2 = np.array([[215,728],[215,670],[285,670],[285,728]],np.int32)
slot3 = np.array([[305,728],[305,670],[375,670],[375,728]],np.int32)
slot4 = np.array([[405,728],[405,670],[475,670],[475,728]],np.int32)
#eslot = np.array([[130,780],[130,755],[165,755],[165,780]],np.int32)
bbox = {'top': 57, 'left': 0, 'width': 420, 'height': 750}

#resizing pct of img
height_percent = 53
width_percent = 60
sct = mss()
last_time = time.time()

def elixerRegion(original_image):
    processed_img = areaOfInterest(original_image)
    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2GRAY)
    return processed_img

def areaOfInterest(img):
    #blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, [slot1],(255,255,255))
    cv2.fillPoly(mask, [slot2],(255,255,255))
    cv2.fillPoly(mask, [slot3],(255,255,255))
    cv2.fillPoly(mask, [slot4],(255,255,255))
    #cv2.fillPoly(mask, [eslot],(255,255,255))

    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked


while True:
    #get screen img
    sct_img = sct.grab(bbox)
    #convert img to array
    screen = np.array(sct_img)
    # resizing the img to fit better on the screen
    width = int(screen.shape[1] * width_percent / 100)
    height = int(screen.shape[0] * height_percent / 100)
    dim = (width, height)
    resized = cv2.resize(screen, dim, interpolation = cv2.INTER_AREA)
    final_screen = elixerRegion(resized)

    check1 = ResizeSlots.firstSlot(final_screen)
    check2 = ResizeSlots.secondSlot(final_screen)
    check3 = ResizeSlots.thirdSlot(final_screen)
    check4 = ResizeSlots.fourthSlot(final_screen)

    print(check_for_match(check1))

    cv2.imshow('screen', final_screen)
    #print(f'running at {1/(time.time()-last_time)} FPS')
    last_time = time.time()
    # quit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    # screen shot slots
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("elixerRegion.png", final_screen)
