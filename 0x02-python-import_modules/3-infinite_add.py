#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    y = 0
    for arg in argv[1:]:
        y += int(arg)
    if y == 0:
        print(0)
    else:
        print(y)
