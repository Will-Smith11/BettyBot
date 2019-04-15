from pynput.keyboard import Key, Controller
import numpy as np
import cv2


keyboard = Controller()
'''
keyboard.press('a')
keyboard.release('a')
'''

from pynput.mouse import Button, Controller
mouse = Controller()

print('The current pointer position is {0}'.format(
    mouse.position))


mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(
    mouse.position))

mouse.move(5, -5)


mouse.press(Button.left)
mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on Mac OSX
mouse.click(Button.left, 2)

# Scroll two steps down
mouse.scroll(0, 2)


def Place_cord_options():
    vertice1 = np.array([[300,590],[300,365],[430,365],[430,590]],np.int32)
    vertice2 = np.array([[65,590],[65,365],[200,365],[200,590]],np.int32)
