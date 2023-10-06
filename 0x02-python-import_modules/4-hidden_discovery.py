#!/usr/bin/python3
if (__name__ == "__main__"):
    import hidden_4
    #  extract all name from modules except those with __
    module_var_names = [
            name for name in dir(hidden_4)
            if not name.startswith('__')
            ]
    #  sort the names
    sort_names = sorted(module_var_names)
    #  print all the sorted values to the stdout
    for name in sort_names:
        print(name)
