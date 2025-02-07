# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 12:48:49 2025

@author: user
"""

import cv2

img_org=cv2.imread("cat.jpg")
cv2.imshow('image', img_org)
cv2.waitKey(0)
