import numpy as np
import RPi.GPIO as gp
import cv2
import os
import sys
import time
import math
import subprocess

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
	
if __name__ == '__main__':
	length_picture = input()
	select_coordinates()
