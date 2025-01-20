

#Effortless Live Video Streaming with OpenCV: Master Your Webcam and Computer Vision
#https://www.youtube.com/watch?v=84DbemsmySU

import cv2
import sys

print("welcome")

from sympy.multipledispatch.dispatcher import source

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv2.VideoCapture(s)

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27:
    has_frame, frame = source.read()
    if not has_frame:
        break

    cv2.imshow(win_name, frame)

source.release()
cv2.destroyWindow(win_name)





