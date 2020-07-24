import os

pics = []
txts = []
os.chdir("../data/img")
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