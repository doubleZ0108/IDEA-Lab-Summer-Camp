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
    dirname = "image/"

    for filename in os.listdir(dirname):
        (name, appidx) = os.path.splitext(dirname + filename)
        if appidx == ".jpg":
            img = np.array(Image.open(dirname + filename)) 

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