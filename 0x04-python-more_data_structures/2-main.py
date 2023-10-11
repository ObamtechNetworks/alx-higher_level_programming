#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
my_list2 = ["Jaguar", "2", 3, 1, 4, 2.2, 5.3]
result = uniq_add(my_list2)
print("Result: {:d}".format(result))
