import os
import RPi.GPIO as gp
import numpy as np
import cv2
import subprocess
import time

######################################
'''
Parameter setting
'''
width  = 240 #320
height = 320 #240
fps = 30
brightness = 50               # min=0   max=100  step=1
contrast = 0                  # min=-100  max=100  step=1
saturation = 0                # min=-100  max=100  step=1
rotate = 0                    # min=0  max=360  step=90 
auto_exposure = 0             # min=0  max=3 
exposure_time_absolute = 1000 # min = 1  max=10000  step=1

#######################################

gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(7,gp.OUT)
gp.setup(11,gp.OUT)
gp.setup(12,gp.OUT)

i2c = "i2cset -y 1 0x70 0x00 0x04"
os.system(i2c)
gp.output(7, False)
gp.output(11, False)
gp.output(12, True)
	
Cam = cv2.VideoCapture(0)
Cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, width)
Cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, height)
Cam.set(cv2.cv.CV_CAP_PROP_FPS, fps)   
command ="v4l2-ctl -d 0 -c brightness=%d" % (brightness)
output = subprocess.call(command, shell=True)
command ="v4l2-ctl -d 0 -c contrast=%d" % (contrast)
output = subprocess.call(command, shell=True)
command ="v4l2-ctl -d 0 -c saturation=%d" % (saturation)
output = subprocess.call(command, shell=True)
command ="v4l2-ctl -d 0 -c rotate=%d" % (rotate)
output = subprocess.call(command, shell=True)
command ="v4l2-ctl -d 0 -c auto_exposure=%d" % (auto_exposure)
output = subprocess.call(command, shell=True)
command ="v4l2-ctl -d 0 -c exposure_time_absolute=%d" % (exposure_time_absolute)
output = subprocess.call(command, shell=True)
ret, frame = Cam.read()
cv2.imshow('img', frame)
a = input()

time.sleep(1)

i2c = "i2cset -y 1 0x70 0x00 0x06"
os.system(i2c)
gp.output(7, False)
gp.output(11, True)
gp.output(12, False)

Cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, width)
Cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, height)
Cam.set(cv2.cv.CV_CAP_PROP_FPS, fps)   
command ="v4l2-ctl -d 0 -c brightness=%d" % (brightness)
output = subprocess.call(command, shell=True)
command ="v4l2-ctl -d 0 -c contrast=%d" % (contrast)
output = subprocess.call(command, shell=True)
command ="v4l2-ctl -d 0 -c saturation=%d" % (saturation)
output = subprocess.call(command, shell=True)
command ="v4l2-ctl -d 0 -c rotate=%d" % (rotate)
output = subprocess.call(command, shell=True)
command ="v4l2-ctl -d 0 -c auto_exposure=%d" % (auto_exposure)
output = subprocess.call(command, shell=True)
command ="v4l2-ctl -d 0 -c exposure_time_absolute=%d" % (exposure_time_absolute)
output = subprocess.call(command, shell=True)
#ret, frame = Cam.read()
#cv2.imshow('img', frame)

#CamR = cv2.VideoCapture(2)
#CamL = cv2.VideoCapture(0)

#index = 0
#while True:
#	retR, frameR = Cam.read()
#	retL, frameL = Cam.read()

#	if index == 0:
#		gp.output(7, False)
#	    gp.output(11, False)
#	    gp.output(12, True)
#	if index == 1:
#	    gp.output(7, False)
#	    gp.output(11, True)
#	    gp.output(12, False)
	
#	cv2.imshow('imgR', frameR)
#	cv2.imshow('imgL', frameL)
	
#	if cv2.waitKey(1) & 0xFF == ord(' '):
#		break
		
#CamR.release()
#CamL.release()
cv2.destroyAllWindows()
