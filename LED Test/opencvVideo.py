import cv2 as cv
import numpy as np
import os
import pyautogui
from time import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

loop_time = time()
while(True):
    
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    # Convert RGB to BGR
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    cv.imshow('Computer Vision', screenshot)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows
print('Done.')
