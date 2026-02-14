import cv2
import numpy as np

def image_to_heightmap(path):
    img = cv2.imread(path, 0)
    img = cv2.resize(img, (200, 200))
    height_map = img / 255.0
    return height_map
