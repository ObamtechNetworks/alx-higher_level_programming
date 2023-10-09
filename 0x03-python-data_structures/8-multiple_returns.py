#!/usr/bin/python3
def multiple_returns(sentence):
    # check if a valid arg (str) is passed
    if type(sentence) == str:
        length = len(sentence)
        if (length == 0):
            first = None
        else:
            first = sentence[:1]
        tupple = length, first
        return tupple
    else:
        raise TypeError("invalid argument: expected a string")
