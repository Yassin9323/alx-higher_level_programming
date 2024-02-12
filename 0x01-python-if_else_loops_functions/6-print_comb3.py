#!/usr/bin/python3
for x in range(10):
    for y in range(x + 1, 10):
        z = x * 10 + y
        print("{:02d}".format(z), end="")
        print(end=", " if z < 89 else "\n")
    # another solution
    # print("{:02d}".format(x * 10 + y)
    # , end="\n" if x == 8 and y == 9 else ", ")
