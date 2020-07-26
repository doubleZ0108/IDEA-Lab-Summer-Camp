import numpy as np
import cv2
from PIL import Image
import shutil

def brightness(img):
    img = Image.fromarray(img)

    brightness = 1 + np.random.randint(1, 9) / 10
    print(brightness)
    brightness_img = img.point(lambda p: p * brightness)

    return Image.fromarray(np.uint8(brightness_img))

def saveBrightnessLabel(name):
    shutil.copyfile(name + ".txt", name + "_brightness.txt")


def darkness(img):
    darkness = np.random.randint(1, 9) / 10
    darkness_img = img * darkness
    return Image.fromarray(np.uint8(darkness_img))

def saveDarknessLabel(name):
    shutil.copyfile(name + ".txt", name + "_darkness.txt")