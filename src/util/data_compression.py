import os
from PIL import Image
import glob

def compress(img):
    w, h = img.size
    compress_img = img.resize((int(w/1.2), int(h/1.2)), Image.ANTIALIAS)
    return compress_img
    


if __name__ == "__main__":
    # dirname = "image/"
    # filename = "test.jpg"

    # os.chdir(dirname)
    # (name, appidx) = os.path.splitext(filename)
    # img = Image.open(filename)

    # compress_img = compress(img)
    # compress_img.save(filename)

    for filepath,dirnames,filenames in os.walk(r'image/'):
        for filename in filenames:
            if filename != "desktop.ini":
                img_path = filepath + "/" + filename
                (name, appidx) = os.path.splitext(img_path)
                img = Image.open(img_path)

                compress_img = compress(img)
                compress_img.save(img_path)
