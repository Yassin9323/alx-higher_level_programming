#!/usr/bin/python3
def uppercase(str):
    for char in str:
        upper = chr(ord(char) - 32) if "a" <= char <= "z" else char
        print("{}".format(upper), end="")
