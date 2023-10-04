#!/usr/bin/python3
'''
Write a program that prints the ASCII alphabet, in reverse order,
alternating lowercase and uppercase
(z in lowercase and Y in uppercase),
not followed by a new line.
------------------------------------------------------
You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store characters in a variable
You are not allowed to import any module

EXPECTED OUTPUT: zYxWvUtSrQpOnMlKjIhGfEdCbA
'''
# THINKING OUT LOUD ... At THIRD STEPS we have the
# UPPERCASE VALUE of the alphabets
# We can start with lowercase using the range of the ascii equivalent numbers
# We can then compare the value whose modulo operation results in even
# to have lowercase while the other in UPPERCASE
# --- blocker: we need to to this in reverse, so this case
# we would use the start stop and step options in the range function
# we would stop at 97, and step -1 at every iteration, this case,
# we get to 97 before 96 so, our loop exits

for c in range(122, 96, -1):
    print("{}".format(
        chr(c) if c % 2 == 0
        else chr(c - 32)
        ), end='')
