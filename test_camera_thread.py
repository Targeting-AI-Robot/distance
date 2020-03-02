import os
import RPi.GPIO as gp
import numpy as np
import cv2
import subprocess
import time
from multiprocessing import Process, Manager

manager = Manager()

######################################
'''
Global parameter setting
'''
args_dict = manager.dict() 
args_dict['width']  = 240 #320
args_dict['height'] = 320 #240
args_dict['fps'] = 30
args_dict['brightness'] = 50               # min=0   max=100  step=1
args_dict['contrast'] = 0                  # min=-100  max=100  step=1
args_dict['saturation'] = 0                # min=-100  max=100  step=1
args_dict['rotate'] = 0                    # min=0  max=360  step=90 
args_dict['auto_exposure'] = 0             # min=0  max=3 
args_dict['exposure_time_absolute'] = 1000 # min = 1  max=10000  step=1

#######################################
'''
GPIO setting
'''
gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(7,gp.OUT)
gp.setup(11,gp.OUT)
gp.setup(12,gp.OUT)

#######################################
'''
Activating cameras, Left and Right camera
'''
def init_Cams(Cam):
	i2c = "i2cset -y 1 0x70 0x00 0x04"
	os.system(i2c)
	gp.output(7, False)
	gp.output(11, False)
	gp.output(12, True)

	Cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, args_dict['width'])
	Cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, args_dict['height'])
	Cam.set(cv2.cv.CV_CAP_PROP_FPS, args_dict['fps'])   
	command ="v4l2-ctl -d 0 -c brightness=%d" % (args_dict['brightness'])
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c contrast=%d" % (args_dict['contrast'])
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c saturation=%d" % (args_dict['saturation'])
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c rotate=%d" % (args_dict['rotate'])
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c auto_exposure=%d" % (args_dict['auto_exposure'])
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c exposure_time_absolute=%d" % (args_dict['exposure_time_absolute'])
	output = subprocess.call(command, shell=True)
	
	time.sleep(1)
	
	i2c = "i2cset -y 1 0x70 0x00 0x06"
	os.system(i2c)
	gp.output(7, False)
	gp.output(11, True)
	gp.output(12, False)

	Cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, args_dict['width'])
	Cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, args_dict['height'])
	Cam.set(cv2.cv.CV_CAP_PROP_FPS, args_dict['fps'])   
	command ="v4l2-ctl -d 0 -c brightness=%d" % (args_dict['brightness'])
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c contrast=%d" % (args_dict['contrast'])
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c saturation=%d" % (args_dict['saturation'])
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c rotate=%d" % (args_dict['rotate'])
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c auto_exposure=%d" % (args_dict['auto_exposure'])
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c exposure_time_absolute=%d" % (args_dict['exposure_time_absolute'])
	output = subprocess.call(command, shell=True)
	
def activate_CamL(Cam):
	CamL = Cam
	while True:
		retL, frameL = CamL.read()
		cv2.imshow('imgL', frameL)
		
		if cv2.waitKey(1) & 0xFF == ord(' '):
			break
	
	Cam .release()
	cv2.destroyAllWindows()
	
def activate_CamR(Cam):
	CamR = Cam
	while True:
		retR, frameR = CamR.read()
		cv2.imshow('imgR', frameR)
		
		if cv2.waitKey(1) & 0xFF == ord(' '):
			break
	
	Cam.release()
	cv2.destroyAllWindows()
	
if __name__ == '__main__':
	Cam = cv2.VideoCapture(0)
	init_Cams(Cam)
	
	gp.output(7, False)
	gp.output(11, False)
	gp.output(12, True)
	pL = Process(target=activate_CamL, args=(Cam,))
	pL.start()
	
	time.sleep(1)
	
	gp.output(7, False)
	gp.output(11, True)
	gp.output(12, False)
	pR = Process(target=activate_CamR, args=(Cam,))
	pR.start()
	
	pL.join()
	pR.join()
