import time
import random
import cv2
import numpy as np
import urllib.request
from PIL import Image
from yolo import YOLO
import string
from urllib.parse import quote

yolo = YOLO()

class Recognition():
    def recognition(self, dataModel):
        image = dataModel['image']
        
        boxs, classes = yolo.detect_image_only_person(image)

        Boxs = []
        personCount = 0
        for i in range(len(classes)):
            objectType = classes[i]
            if objectType == 'person':
                personCount += 1
        
        dataModel['recognitionTags'].append(
            {
                'name':'recognition',
                'personCount': personCount,
                'algorithm': 'YOLOv3',
                'timestamp': int(time.time())
            }
        )
        return True