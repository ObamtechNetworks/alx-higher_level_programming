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

    # case 1: check for type of text (input) is 'str'
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Convert the text to a list of characters for manipulation
    text_cpy = list(text)

    # set flag to track if newline has been added
    added_newline = False

    chars_to_find = ['.', '?', ':']
    # Iterate through the list and add 2 new lines after '.', '?', or ':'
    for index, char in enumerate(text_cpy):
        # check if each char from text matches chars in the list
        # also check if newline has not been added already
        if char in chars_to_find and not added_newline:
            # check the index of the char to avoid index error
            if index < len(text_cpy) - 1:
                text_cpy.insert(index + 1, '\n\n')
            else:
                text_cpy.append('\n\n')
            added_newline = True
        else:
            # Reset the flag if a non-special character is encountered
            added_newline = False

    # Convert list back to str and rem spaces at the beg/end of each line
    filtered = [line.strip() for line in ''.join(text_cpy).split('\n')]

    # join filtered text
    join_filtered = '\n'.join(filtered)
    print(join_filtered, end='')
