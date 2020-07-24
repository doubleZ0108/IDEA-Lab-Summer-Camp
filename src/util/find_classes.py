import os

max = 0
save_name = ""

os.chdir("../data/img")
for filename in os.listdir(os.getcwd()):
    (name, appidx) = os.path.splitext(filename)

    if appidx == ".txt":
        with open(filename, "r") as file:
            line = file.readline()
            num = int(line[0])
            if num > max:
                max = num
                save_name = name

print(max)
print(save_name)
            