import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 30
camera.rotation = 180
rawCapture = PiRGBArray(camera)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

        lower_range = np.array([29,86,6])
        upper_range = np.array([64,255,255])

        mask = cv2.inRange(hsv,lower_range,upper_range)

        moments = cv2.moments(mask)

        #cv2.imshow('normal', image)
        cv2.imshow('gray', hsv)
        cv2.imshow('mask', mask)

        key=cv2.waitKey(1)



        rawCapture.truncate(0)

        if key == 27:
            camera.close()
            cv2.destroyAllWindows()
            break
