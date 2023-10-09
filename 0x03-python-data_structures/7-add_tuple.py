#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # argument validation (arguments must be tuples
    if type(tuple_a == tuple) and type(tuple_b == tuple):
        # edge cases if tuples are empty
        if len(tuple_a) == 0 and len(tuple_b) != 0:
            return (tuple_b)
        elif len(tuple_b) == 0 and len(tuple_a) != 0:
            return (tuple_a)
        elif len(tuple_a) == 0 and len(tuple_b) == 0:
            return (0, 0)
        # get only two el from the tuple, concat 0 tuple as arg if need be
        tup_a = tuple_a[:2] + (0,) * len(tuple_a)
        tup_b = tuple_b[:2] + (0,) * len(tuple_b)
        # since it's just list of len 2, we can just access index directly
        # however we want to get the type validation too
        # let's add them only if types are valid, else raise TypeError
        try:
            new_tuple = (tup_a[0] + tup_b[0], tup_a[1] + tup_b[1])
        except TypeError as e:
            print(f"TypeError: {e} - Value: {item}")
        return new_tuple  # return the new tuple
    else:
        return (0, 0)
