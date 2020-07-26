import os
import shutil
import numpy as np
from PIL import Image

from noise import *
from flip import *
from sharpen import *
from blur import *
from crop import *
from cutout import *
from lightness import *
from contrast import *
from deform import *
from distortion import *
from vignetting import *

if __name__ == "__main__":
    dirname = "src/data-augmentation/"
    filename = "demo.jpg"

    os.chdir(dirname)
    (name, appidx) = os.path.splitext(filename)
    img = np.array(Image.open(filename)) 

    '''需要重新标注'''
    # crop
    crop_img = crop(np.copy(img))
    crop_img.save(name + "_crop" + appidx)

    # deform
    deform_img = deform(np.copy(img))
    deform_img.save(name + "_deform" + appidx)

    # distortion
    distortion_img = distortion(np.copy(img))
    distortion_img.save(name + "_distortion" + appidx)


    '''自动计算变换后的标签位置'''
    # noise
    noise_img = addNoise(np.copy(img))
    noise_img.save(name + "_noise" + appidx)
    saveNoiseLabel(name)

    # flip
    flip_img = flip(np.copy(img))
    flip_img.save(name + "_flip" + appidx)
    saveFlipLabel(name)

    # sharpen
    sharpen_img = sharpen(np.copy(img))
    sharpen_img.save(name + "_sharpen" + appidx)
    saveSharpenLabel(name)

    # blur
    blur_img = blur(np.copy(img))
    blur_img.save(name + "_blur" + appidx)
    saveBlurLabel(name)

    # cutout
    cutout_img = cutout(np.copy(img))
    cutout_img.save(name + "_cutout" + appidx)
    saveCutoutLabel(name)

    # lightness
    ## brightness
    brightness_img = brightness(np.copy(img))
    brightness_img.save(name + "_brightness" + appidx)
    saveBrightnessLabel(name)

    ## darkness
    darkness_img = darkness(np.copy(img))
    darkness_img.save(name + "_darkness" + appidx)
    saveDarknessLabel(name)

    # contrast
    contrast_img = contrast(np.copy(img))
    contrast_img.save(name + "_contrast" + appidx)
    saveContrastLabel(name)

    # vignetting
    vignetting_img = vignetting(np.copy(img))
    vignetting_img.save(name + "_vignetting" + appidx)
    saveVignettingLabel(name)
