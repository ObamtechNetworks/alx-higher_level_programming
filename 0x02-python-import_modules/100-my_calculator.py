#!/usr/bin/python3
if __name__ == "__main__":  # will not run when imported itno another file
    import sys
    from calculator_1 import add, sub, mul, div  # imports functions
    # get the command line arguments
    args = sys.argv  # command line argument
    argc = len(args)  # length of CLI args

    # check for length of command line arguments
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(args[1])  # first operand
    op = args[2]  # operator
    b = int(args[3])  # second operand
    operators = ['+', '-', '/', '*']

    # print the operation if all is satisfied
    if op == operators[0]:
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op == operators[1]:
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    elif op == operators[2]:
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
    elif op == operators[3]:
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    else:
        if op not in operators:  # invalid operators
            print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
