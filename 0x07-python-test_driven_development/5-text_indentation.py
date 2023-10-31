#!/usr/bin/python3
"""
This module defines a function that prints a text with 2 new lines

The new lines are printed after each of these characters: '.', '?', and ':'
Function prototype: def text_indenation(text):
-> text must be a string, else TypeError exception is raised
For every line printed, there is no space at the beg. or end of each line

Returns:
    Nothing
"""
def text_indentation(text):
    """
    This function prints a text with 2 new lines after char: '.', '?', ':'

    Args:
        text (str): must be a string

    No space at the beg. or end of each printed line

    Returns:
        None
    """
    # case 1: check for type of text if 'str'
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # make a copy of the text into a list
    text_cpy = list(text)
    # all occurrence to find
    chars_to_find = ['.', '?', ':']
    new_text = []

    # loop through the text copy and match each char
    for index, char in enumerate(text):
        if char in chars_to_find:
            # replace space char after index with newline
            if index + 1 < len(text_cpy):
                text_cpy[index + 1] = '\n\n'
            elif index == len(text_cpy) - 1:
                text_cpy.append('\n\n')

    # strip spaces from beg and end
    text_cpy = [line.strip() for line in ''.join(text_cpy).split('\n')]
    filtered = '\n'.join(text_cpy)
    # join the list back into a string
    print(filtered, end='')
