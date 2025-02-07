# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 12:48:49 2025

@author: user
"""

import cv2

cap = cv2.VideoCapture(0) 
while True:
	# capture image
	ret, img_org = cap.read()
#	cv2.imshow('image', img_org)
	key = cv2.waitKey(1)
	if key == 27: # ESC
		break
    
	cv2.imwrite('output.jpg', img_org)
	cv2.imshow('image', img_org)
		
cap.release()
cv2.destroyAllWindows()