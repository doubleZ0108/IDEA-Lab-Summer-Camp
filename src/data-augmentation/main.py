import os
import shutil
import numpy as np
from PIL import Image

from noise import *
from flip import *

if __name__ == "__main__":
    dirname = "src/data-augmentation/"
    filename = "test.jpg"

    os.chdir(dirname)
    (name, appidx) = os.path.splitext(filename)
    img = np.array(Image.open(filename)) 

    # noise
    noise_img = addNoise(img)
    noise_img.save(name + "_noise" + appidx)
    saveNoiseLabel(name)

    # flip
    flip_img = flip(img)
    flip_img.save(name + "_flip" + appidx)
    saveFlipLabel(name)