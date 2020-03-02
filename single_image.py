import numpy as np
import RPi.GPIO as gp
import cv2
import os
import sys
import time
import math
import subprocess

##########################################

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

gp.setup(15, gp.OUT)
gp.setup(16, gp.OUT)
gp.setup(21, gp.OUT)
gp.setup(22, gp.OUT)

gp.output(11, True)
gp.output(12, True)
gp.output(15, True)
gp.output(16, True)
gp.output(21, True)
gp.output(22, True)

##########################################
'''
Define functions
'''
def event_callback(event,x,y,flages,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print("X :", x, ", Y : ", y)
			
def image_test():
	i2c = "i2cset -y 1 0x70 0x00 0x04"
    
	os.system(i2c)
	gp.output(7, False)
	gp.output(11, False)
	gp.output(12, True)
	
	capture(1)
	
	cv2.namedWindow('Image Test',cv2.WINDOW_NORMAL)
	cv2.setMouseCallback('Image Test', event_callback)
	
	test_img = cv2.imread("capture_1.jpg")
	cv2.resizeWindow('Image Test',820,616)
	cv2.imshow('Image Test',test_img)
	
	cv2.waitKey()
	
def capture(cam):
    cmd = "raspistill -w 1640 -h 1262 -o capture_%d.jpg" % cam
    os.system(cmd)
	
if __name__ == '__main__':
	image_test()
