# -*- coding: utf-8 -*-
import cv2
import tensorflow as tf
import numpy as np
import os

# Path to label map file
PATH_TO_LABELS = os.path.join('labelmap.txt')

# Load the label map
with open(PATH_TO_LABELS, 'r') as f:
    labels = [line.strip() for line in f.readlines()]

if labels[0] == '???':
    del(labels[0])

# load model
interpreter = tf.lite.Interpreter(model_path="detect.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

cap = cv2.VideoCapture(0) 
while True:
	# capture image
	ret, img_org = cap.read()
#	cv2.imshow('image', img_org)
	key = cv2.waitKey(1)
	if key == 27: # ESC
		break

	# prepara input image
	img = cv2.cvtColor(img_org, cv2.COLOR_BGR2RGB)
	img = cv2.resize(img, (300, 300))
	img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2]) # (1, 300, 300, 3)
	img = img.astype(np.uint8)
		
	
