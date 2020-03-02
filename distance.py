import numpy as np
import RPi.GPIO as gp
import cv2
import os
import sys
import time
import math
import subprocess

##########################################
'''
Parameters for camera
'''
rx = 3280       #resolution for X
ry = 2464       #resolution for Y
cx = rx//2		#principal point for X
cy = ry//2		#principal point for Y

##########################################
'''
GPIO initialize
'''
gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(7,gp.OUT)
gp.setup(11,gp.OUT)
gp.setup(12,gp.OUT)

##########################################
'''
Define functions
'''
def event_callback(event,x,y,flages,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print("X :", x, ", Y : ", y)

def capture_test():
	cam = cv2.VideoCapture(0)
	cam.set(3, rx)
	cam.set(4, ry)
	
	cv2.namedWindow('Video Test')
	cv2.setMouseCallback('Video Test', event_callback)
	
	while True:
		_, frame = cam.read()
		cv2.imshow('Video Test', frame)
		
		if cv2.waitKey(1) & 0xFF == ord(' '):
			break
			
	cam.release()
	cv2.destroyAllWindows()
			
def image_test():
	i2c = "i2cset -y 1 0x70 0x00 0x04"
    
	os.system(i2c)
	gp.output(7, False)
	gp.output(11, False)
	gp.output(12, True)
	
	img = cv2.VideoCapture(0)
	
	cv2.namedWindow('Image Test',cv2.WINDOW_NORMAL)
	cv2.setMouseCallback('Image Test', event_callback)
	
	_, frame = img.read()
	cv2.imwrite("image_test.jpg", frame)
	
	test_img = cv2.imread("capture_1.jpg")
	cv2.resizeWindow('Image Test',1640,1232)
	cv2.imshow('Image Test',test_img)
	
	cv2.waitKey()
	
if __name__ == '__main__':
	#capture_test()
	image_test()
