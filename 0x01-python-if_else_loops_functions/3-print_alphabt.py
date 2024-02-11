#!/usr/bin/python3
letter = "q , e"
for i in range(97, 123):
    if i != letter:
        print("{}".format(chr(i)), end="")
