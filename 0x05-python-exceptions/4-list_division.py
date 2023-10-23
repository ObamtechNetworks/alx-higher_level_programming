#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    division = 0
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
            new_list.append(division)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
    return new_list
