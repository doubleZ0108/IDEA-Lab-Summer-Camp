import numpy as np
import cv2
from PIL import Image
import shutil

'''
图像拉伸
'''
def deform(img):
    img = Image.fromarray(img)
    w, h = img.size[:2]

    # 拉伸成宽为w的正方形
    deform_img = img.resize((int(w), int(w)))

    return deform_img
    
