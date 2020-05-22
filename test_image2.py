import numpy as np
import cv2

img = cv2.imread('demo.png')
img_rbg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(type(img)) 
