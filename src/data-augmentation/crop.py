import numpy as np
import cv2
from PIL import Image
import shutil

def crop(img):
    size = img.shape[:2]
    kernel_size = list(map(lambda x: int(x*0.8), size))
    shift_min, shift_max = -50, 50
    shift_size = [np.random.randint(shift_min, shift_max), np.random.randint(shift_min, shift_max)]

    crop_img = img[
        (size[0]-kernel_size[0])//2+shift_size[0]:(size[0]-kernel_size[0])//2+kernel_size[0]+shift_size[0],
        (size[1]-kernel_size[1])//2+shift_size[1]:(size[1]-kernel_size[1])//2+kernel_size[1]+shift_size[1]
    ]
    
    return Image.fromarray(np.uint8(crop_img))
