import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
while (true):
	# capture frame by frame
	ret, frame = cap.read()

	# operation on frame
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	# Display the frame
	cv2.imgshow('frame',gray)
	key = cv2.waitKey(0)
	if key == ord('q'):
		break


cv2.release()
cv2.distroyAllWindows()	
