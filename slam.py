#!/usr/bin/env python3
import cv2
import numpy as np
  
W = 1920//2
H = 1080//2

cap = cv2.VideoCapture("test.mp4")
orb = cv2.ORB_create()
if cap.isOpened() == False:
  print("Error opening video stream or file")

while cap.isOpened():
  ret, frame = cap.read()
  if ret == True:
    frame = cv2.resize(frame, (W,H))
    kp = orb.detect(frame,None)
    kp, des = orb.compute(frame, kp)
    frame = cv2.drawKeypoints(frame, kp, None, color=(0,255,0), flags=0)
    cv2.imshow('Frame',frame)
    if cv2.waitKey(15) & 0xFF == ord('q'):
      break
  else:
    break

cap.release()
cv2.destroyAllWindows()
