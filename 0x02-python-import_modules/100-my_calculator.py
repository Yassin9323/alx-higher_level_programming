#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as x
    from sys import argv

    num_argv = len(argv) - 1

    if num_argv != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    s = argv[2]

    if s == "+":
        result = x.add(a, b)
    elif s == "-":
        result = x.sub(a, b)
    elif s == "*":
        result = x.mul(a, b)
    elif s == "/":
        result = x.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(a, s, b, "=", result)
