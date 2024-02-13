#!/usr/bin/python3
def fizzbuzz():
    for x in range(101):
        if x % 3 == 0 and x % 5 == 0 and x != 0:
            print("fizzbuzz", end=" ")
        elif x % 3 == 0 and x != 0:
            print("Fizz", end=" ")
        elif x % 5 == 0 and x != 0:
            print("buzz", end=" ")
        else:
            print("{:02d}".format(x), end=" ")


fizzbuzz()
