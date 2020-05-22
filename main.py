import cv2
import myyolov3
from PIL import Image


image = cv2.imread('demo.png')
image2 = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
test = myyolov3.Recognition()
test.recognition(image2)

