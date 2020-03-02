import cv2

def event_callback(event,x,y,flages,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print("X :", x, ", Y : ", y)	

if __name__ == '__main__':
	img_L = cv2.imread('capture_L.jpg')
	img_R = cv2.imread('capture_R.jpg')

	cv2.namedWindow('Left')
	cv2.namedWindow('Right')

	cv2.setMouseCallback('Left', event_callback)
	cv2.setMouseCallback('Right', event_callback)


	cv2.resizeWindow('Left', 820, 616)
	cv2.imshow('Left', img_L)
	cv2.resizeWindow('Right', 820, 616)
	cv2.imshow('Right', img_R)

	cv2.waitKey()
