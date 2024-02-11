#!/usr/bin/python3
letter = "q, e"
for i in range(97, 123):
    if chr(i) not in letter:
        print("{}".format(chr(i)), end="")
