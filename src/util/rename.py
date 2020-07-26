import os

if __name__ == "__main__":
    for filepath,dirnames,filenames in os.walk(r'image/'):
        counter = 0
        for filename in filenames:
            if filename != "desktop.ini":
                img_path = filepath + "/" + filename
                (name, appidx) = os.path.splitext(img_path)

                os.rename(img_path, filepath+"_"+str(counter)+appidx)                
                counter = counter + 1
