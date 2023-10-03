#!/usr/bin/python3
with open('main.py', 'r') as file:
    source = file.read()

# Comiile the source code into bytecode using the compile function
compiled_code = compile(source, 'main.py', 'exec')

# Write the compiled bytecode to a .pyc file in binary form
with open('main.pyc', 'wb') as pyc_file:
    pyc_file.write(compiled_code.co_code)

# print compiling message
print('Compiling main.py ...')
