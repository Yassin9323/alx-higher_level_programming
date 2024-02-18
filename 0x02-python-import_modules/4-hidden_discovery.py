#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    args = dir(hidden_4)
    for x in sorted(args):
        if not x.startswith("__"):
            print(x)
