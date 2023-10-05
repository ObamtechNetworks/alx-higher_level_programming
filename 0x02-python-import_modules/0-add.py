#!/usr/bin/python3
if __name__ == "__main__":  # will not run when imported into another file
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
