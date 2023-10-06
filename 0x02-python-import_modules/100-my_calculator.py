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
 
    # check if valid operator is given
    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # print the operation if all is satisfied
    print("{} {} {} = {}".format(a, op, b, add(a, b)))
