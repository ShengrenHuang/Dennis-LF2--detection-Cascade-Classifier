import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision



os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture('Little Fighter 2')

cascade_Dennis = cv.CascadeClassifier('cascade/cascade.xml')

vision_Dennis = Vision(None)

loop_time = time()

while(True):

    screenshot = wincap.get_screenshot()


    rectangles = cascade_Dennis.detectMultiScale(screenshot)

    detection_image = vision_Dennis.draw_rectangles(screenshot, rectangles)

    cv.imshow('Matches', detection_image)

    print('FPS {}'.format(1/(time() - loop_time)))
    loop_time = time()

    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord('f'):
        cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
    elif key == ord('d'):
        cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)

print('Done.')