import numpy as np
import RPi.GPIO as gp
import cv2
import os
import sys
import time
import math
import subprocess

######################################
'''
Parameter setting
'''
width  = 1280
height = 1280 

######################################
'''
GPIO initialize
'''
gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(7,gp.OUT)
gp.setup(11,gp.OUT)
gp.setup(12,gp.OUT)

######################################
'''
Functions
'''
def take_L_image():
	global length_picture
	i2c = "i2cset -y 1 0x70 0x00 0x04"
    
	os.system(i2c)
	gp.output(7, False)
	gp.output(11, False)
	gp.output(12, True)
	
	cap = cv2.VideoCapture(0)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
	
	rev, frame = cap.read()
	#resized = cv2.resize(frame, (512,512), interpolation=cv2.INTER_AREA)
	#cv2.imwrite('capture_L'+length_picture+'.png', resized)
	cv2.imwrite(os.path.join('/home/pi/Desktop/example/distance_img','capture_L_'+length_picture+'.png'), frame)
    
def take_R_image():
	global length_picture
	i2c = "i2cset -y 1 0x70 0x00 0x06"
        
	os.system(i2c)
	gp.output(7, False)
	gp.output(11, True)
	gp.output(12, False)
    
	cap = cv2.VideoCapture(0)
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
	
	rev, frame = cap.read() 
	#resized = cv2.resize(frame, (512,512), interpolation=cv2.INTER_AREA)
	#cv2.imwrite('capture_R.png', resized)
	cv2.imwrite(os.path.join('/home/pi/Desktop/example/distance_img','capture_R_'+length_picture+'.png'), frame)
 
def event_callback(event,x,y,flages,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print("X :", x, ", Y : ", y)	
		
def select_coordinates():
	global length_picture		
	cv2.namedWindow('Left',cv2.WINDOW_NORMAL)
	cv2.namedWindow('Right',cv2.WINDOW_NORMAL)
	
	img_L = cv2.imread('distance_img/capture_L_'+length_picture+'.png')
	img_R = cv2.imread('distance_img/capture_R_'+length_picture+'.png')
	
	cv2.setMouseCallback('Left', event_callback)
	cv2.setMouseCallback('Right', event_callback)
	
	cv2.imshow('Left', img_L)
	cv2.resizeWindow('Left', 640, 640)
	cv2.imshow('Right', img_R)
	cv2.resizeWindow('Right', 640, 640)
	
	cv2.waitKey()
    
######################################

if __name__ == '__main__':
	length_picture = input()
	take_L_image()
	take_R_image()
	#select_coordinates()
