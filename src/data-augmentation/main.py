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
    filename = "test.jpg"

    os.chdir(dirname)
    (name, appidx) = os.path.splitext(filename)
    img = np.array(Image.open(filename)) 

    # # crop
    # crop_img = crop(img)
    # crop_img.save(name + "_crop" + appidx)

    # # deform
    # deform_img = deform(img)
    # deform_img.save(name + "_deform" + appidx)

    # # distortion
    # distortion_img = distortion(img)
    # distortion_img.save(name + "_distortion" + appidx)



    # # noise
    # noise_img = addNoise(img)
    # noise_img.save(name + "_noise" + appidx)
    # saveNoiseLabel(name)

    # # flip
    # flip_img = flip(img)
    # flip_img.save(name + "_flip" + appidx)
    # saveFlipLabel(name)

    # # sharpen
    # sharpen_img = sharpen(img)
    # sharpen_img.save(name + "_sharpen" + appidx)
    # saveSharpenLabel(name)

    # # blur
    # blur_img = blur(img)
    # blur_img.save(name + "_blur" + appidx)
    # saveBlurLabel(name)

    # # cutout
    # cutout_img = cutout(img)
    # cutout_img.save(name + "_cutout" + appidx)
    # saveCutoutLabel(name)

    # lightness
    # ## brightness
    # brightness_img = brightness(img)
    # brightness_img.save(name + "_brightness" + appidx)
    # saveBrightnessLabel(name)

    ## darkness
    # darkness_img = darkness(img)
    # darkness_img.save(name + "_darkness" + appidx)
    # saveDarknessLabel(name)

    # contrast
    # contrast_img = contrast(img)
    # contrast_img.save(name + "_contrast" + appidx)
    # saveContrastLabel(name)

    # vignetting
    vignetting_img = vignetting(img)
    vignetting_img.save(name + "_vignetting" + appidx)
    saveVignettingLabel(name)
