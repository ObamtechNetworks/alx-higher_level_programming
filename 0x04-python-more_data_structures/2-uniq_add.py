#!/usr/bin/python3
def uniq_add(my_list=[]):
    # do operation if list is not empty
    if len(my_list) > 0:
        try:
            # generate a unique version of the list
            unique = set()
            sums = 0
            # iterate through the list to sum values
            for x in my_list:
                if isinstance(x, int):  # select only integers
                    unique.add(x)  # add the element to the set
            # sum all the element of the set
            sums = sum(unique)
            return sums
        except (ValueError, TypeError) as e:
            raise e("Invalid arguments")
    else:
        raise TypeError("Expected a list")
