"""
根据文件夹中的图像和txt数据生成训练列表
"""

import os

img_dirs = ['main', 'man_labled', 'auto_generated', 'previous']

with open("data/list.txt", "w") as outfile:
    for img_dir in img_dirs:
        image_files = []
        os.chdir("data/" + img_dir + "/")
        for filename in os.listdir(os.getcwd()):
            if not filename.endswith(".txt") and filename != ".DS_Store":
                # image_files.append("../../data/img/" + filename)
                outfile.write("../../data/"+img_dir+"/" + filename + "\n")
        os.chdir("../../")