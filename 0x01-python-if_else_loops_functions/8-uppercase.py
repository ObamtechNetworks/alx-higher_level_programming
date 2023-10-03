#!/usr/bin/python3
''' loop through indvidual characters in str,
check if they are lowercase, using the ord() function logic
and then convert them to UPPERCASE by subtracting integer 32
form the ord() function. i.e: (ord(c) - 32), the rt val is
passed as argument to the chr() function
which returns equivalent character in uppercase.
'''


def uppercase(str):
    for c in str:
        if (ord(c) >= 97):
            c = chr(ord(c) - 32)
        print('{}'.format(c), end='')
    print()
