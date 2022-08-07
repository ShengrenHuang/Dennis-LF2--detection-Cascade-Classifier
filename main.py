import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
#from vision import Vision



os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture('Little Fighter 2')

loop_time = time()

while(True):

    screenshot = wincap.get_screenshot()

    cv.imshow('Unprocessed', screenshot)

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