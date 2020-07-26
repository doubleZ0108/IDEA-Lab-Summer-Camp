import shutil, os

if __name__ == "__main__":
    dirname = "image/origin/"
    fresh_dirname = "image/origin/"

    for filename in os.listdir(dirname):
        (name, appidx) = os.path.splitext(dirname + filename)
        if appidx == ".jpg":
            if name[-1].isdigit():
                freshname = filename[6:]
                shutil.move(dirname + filename, fresh_dirname + freshname)
