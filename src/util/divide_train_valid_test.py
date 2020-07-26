import os

if __name__ == "__main__":

    train, valid, test = 8, 1, 1
    # train, valid, test = 6, 2, 2

    counter = 0
    with open("data/list.txt", "r") as list:
        for line in list.readlines():
            counter = counter + 1

    with open("data/train.txt", "w") as train, open("data/valid.txt", "w") as valid, open("data/test.txt", "w") as test:
        with open("data/list.txt", "r") as list:
            index = 0
            for line in list.readlines():
                last_num = int(str(index)[-1])
                
                if last_num == 8:
                    valid.write(line)
                elif last_num == 9:
                    test.write(line)
                else:
                    train.write(line)

                index = index + 1