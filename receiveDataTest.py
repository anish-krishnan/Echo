import cv2
import numpy as np
import urllib


url = 'tcp://10.251.83.165:8081'
cap = cv2.VideoCapture(url)
while True:
    _, stream = cap.read()
    cv2.imshow('stream',stream)
    if(cv2.waitKey(1) == ord('x')):
    	cv2.destroyWindow('stream')
    	break
