import numpy as np
import cv2
from mss import mss
import time

# location of the screen grab image
bbox = {'top': 57, 'left': 0, 'width': 420, 'height': 750}
#resizing pct of img
height_percent = 53
width_percent = 60
sct = mss()
last_time = time.time()



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
    #final_screen = process_img(resized)

    processed_img = cv2.cvtColor(resized, cv2.COLOR_RGB2BGR)

    cv2.imshow('screen', processed_img)
    print(f'running at {1/(time.time()-last_time)} FPS')
    last_time = time.time()
    # quit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
