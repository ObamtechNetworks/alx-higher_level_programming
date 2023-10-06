#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sums = 0  # defines the starting point of adding values
    # get all CLI arguments
    args = sys.argv
    # convert each argument to numbers
    numbers = []  # create an empty list
    for arg in args:
        if args.index(arg) == 0:  # skip first index - prg name
            continue
        numbers.append(int(arg))
    # get the number of arguments except the name of program
    argc = len(numbers)
    # add all arguments given
    # loop through each arguments and add them up
    for i in range(argc):
        sums = sums + numbers[i]
    print(sums)
