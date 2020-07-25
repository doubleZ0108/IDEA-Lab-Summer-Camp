# coding=utf-8
from PIL import Image
import numpy as np
import shutil

'''
_noise
为图像添加噪声
    随机生成5000个椒盐
'''
def addNoise(img):
    rows,cols,dims = img.shape
    for i in range(5000):
        x = np.random.randint(0,rows)
        y = np.random.randint(0,cols)
        img[x,y,:] = 255
    img.flags.writeable = True  # 将数组改为读写模式
    dst = Image.fromarray(np.uint8(img))
    return dst

def saveNoiseLabel(name):
    shutil.copyfile(name + ".txt", name + "_noise.txt")