"""
一一匹配图像和label，并删除多余的数据
"""

import os

pics = []
txts = []
os.chdir("data/hhh/")
for filename in os.listdir(os.getcwd()):
    (name, appidx) = os.path.splitext(filename)

    if appidx == ".txt":
        txts.append(name)
    else:
        pics.append(name)

result = list(set(pics) & set(txts))

for filename in os.listdir(os.getcwd()):
    (name, appidx) = os.path.splitext(filename)
    if name not in result:
        os.remove(filename)