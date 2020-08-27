import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def findLED(lamp_img_path, led_img_path, threshold=0.55, debug_mode=None):

    lamp_img = cv.imread(lamp_img_path, cv.IMREAD_UNCHANGED)
    led_img = cv.imread(led_img_path, cv.IMREAD_UNCHANGED)

    led_w = led_img.shape[1]
    led_h = led_img.shape[0]

    # Find result using TM_CCOEFF_NORMED
    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(lamp_img, led_img, method)

    # threshold = 0.80
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    print(locations)

    # create the list of [x, y, w, h] rectangles
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), led_w, led_h]
        rectangles.append(rect)
        rectangles.append(rect)


    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
    print(rectangles)

    points = []
    if len(rectangles):
        print('Found LED')

        line_color = (0, 0, 255)
        line_type = cv.LINE_4
        marker_colour = (0, 0, 0)
        marker_type = cv.MARKER_CROSS

        for (x, y, w, h) in rectangles:

            # Determine center position
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            # append 
            points.append((center_x, center_y))

            if debug_mode == 'rectangles':
                # Determine box positions
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                # Draw the box
                cv.rectangle(lamp_img, top_left, bottom_right, line_color, line_type)
            elif debug_mode == 'points':
                cv.drawMarker(lamp_img, (center_x, center_y), marker_colour, marker_type)

        if debug_mode:
            cv.imshow('Matches', lamp_img)
            cv.waitKey()
    return points

points = findLED(r'C:\Users\User\Desktop\Project\Phyton\images\lamp.png', r'C:\Users\User\Desktop\Project\Phyton\images\led.png', debug_mode='points')
print(points)

