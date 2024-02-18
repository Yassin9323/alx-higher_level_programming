#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_args = len(argv) - 1
    if num_args == 1:
        print(num_args, "argument:")
    elif num_args == 0:
        print(num_args, "arguments.")
    else:
        print(num_args, "arguments:")
    for x, arg in enumerate(argv[1:], start=1):
        print(f"{x}: {arg}")
