import os

image_files = []
os.chdir("../data/img")
for filename in os.listdir(os.getcwd()):
    if not filename.endswith(".txt") and filename != ".DS_Store":
        image_files.append("data/img/" + filename)
os.chdir("..")

with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")