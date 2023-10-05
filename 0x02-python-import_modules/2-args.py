#!/usr/bin/python3
if __name__ == "__main__":
    import sys  # through this we can get list of CLI arguments

    args = sys.argv  # returns a list of arguments
    length = len(args)  # this way we get the list of arguments

    # case if length is 0 or NULL (None in python)
    if length == 1:
        length = 0
        print("{} arguments.".format(length))
    elif length == 2:
        length = length - 1
        print("{} argument:".format(length))
    else:
        length = length - 1
        print("{} arguments:".format(length))
    #  loop through arguments length
    for i in range(1, length + 1):
        print("{}: {}".format(i, args[i]))
