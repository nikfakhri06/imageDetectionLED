import cv2 as cv
import numpy as np

lamp_img = cv.imread(r'C:\Users\User\Desktop\Project\Phyton\images\lamp.png', cv.IMREAD_UNCHANGED)
led_img = cv.imread(r'C:\Users\User\Desktop\Project\Phyton\images\led.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(lamp_img, led_img, cv.TM_CCOEFF_NORMED)


min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match top left location: %s' %str(max_loc))
print('Best match confidence: %s' % max_val)

threshold = 0.8
if max_val >= threshold:
    print('Found needle.')

    led_w = led_img.shape[1]
    led_h = led_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0] + led_w, top_left[1] + led_h)

    cv.rectangle(lamp_img, top_left, bottom_right, color=(0,0,255), thickness=2, lineType=cv.LINE_4)

    cv.imshow('Result', lamp_img)
    cv.waitKey()
else:
    print('Needle not found.')



# cv.imshow('Result', result)
# cv.waitKey()