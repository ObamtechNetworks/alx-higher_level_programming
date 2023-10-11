#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # do operation if it's not an empty list and search is in list
    if len(my_list) > 0 and search in my_list:
        new_list = []  # create a new list
        for x in my_list:
            # at pos. of iteration, repl elem if it's equal to search
            if x == search:
                x = replace
            # append items to new list
            new_list.append(x)
        return new_list
    else:
        return my_list
