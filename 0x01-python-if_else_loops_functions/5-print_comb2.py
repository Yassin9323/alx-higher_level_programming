#!/usr/bin/python3
for x in range(100):
    if x < 10:
        print("0" + "{}".format(str(x)), end=", ")
    else:
        ## print("{}".format(str(x)) + "\n" if x == 99 else x, end=", ")
        print(x, end=", " if x < 99 else "\n")
