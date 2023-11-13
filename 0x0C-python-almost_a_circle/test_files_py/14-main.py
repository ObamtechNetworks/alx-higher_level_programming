#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))

    r1 = Rectangle(10, 7, 2, 8, 6)
    my_dict_list = list(r1.to_dictionary())
    print("my_dict_list: ", my_dict_list)
    my_dict_l = [r1.to_dictionary()]
    print("my_dict_l: ", my_dict_l)
    print(len(Base.to_json_string(my_dict_list)))
    print(len(Base.to_json_string(my_dict_l)))

    s1 = Square(10, 2, 3, 4)
    s_json_dict = Base.to_json_string([s1.to_dictionary()])
    print("s_json_dict: ", s_json_dict)
    print(len(s_json_dict))

    s1 = Square(10, 2, 3, 4)
    s2 = Square(1, 4, 3, 3)
    list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
    print(len(Base.to_json_string(list_dicts)))
