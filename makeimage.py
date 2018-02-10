import math
import random

def rand():
    ret = ""
    for i in range(3):
        ret += str(random.randint(0, 256)) + " "
        ret += "\n"
    return ret

def write_to_file():
    file = open("image.ppm", "w+")
    file.write("P3\n")
    file.write("500 500\n")
    file.write("255\n")
    list = []
    r = 176
    g = 196
    b = 222
    for i in range(500):
        list.append([])
        for j in range(500):
            list[i].append("%s %s %s  " % (r, g, b))
            r-=1
            g-=1
            b-=1
            file.write(list[i][j])
        file.write("\n")
    file.close()

write_to_file()
