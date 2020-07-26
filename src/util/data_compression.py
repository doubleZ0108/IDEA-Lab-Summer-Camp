import os
from PIL import Image
import glob

def compress(img):
    w, h = img.size
    compress_img = img.resize((int(w/1.2), int(h/1.2)), Image.ANTIALIAS)
    return compress_img
    


if __name__ == "__main__":
    dirname = "src/util/"
    filename = "large.jpg"

    os.chdir(dirname)
    (name, appidx) = os.path.splitext(filename)
    img = Image.open(filename)

    compress_img = compress(img)
    compress_img.save(name+"_compress"+appidx)