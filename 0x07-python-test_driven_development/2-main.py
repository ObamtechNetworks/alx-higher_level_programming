#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

try:
    print(matrix_divided(10))
except Exception as e:
    print(str(e))

try:
    print(matrix_divided([]))
except Exception as e:
    print(str(e))

try:
    print(matrix_divided('234', 12))
except Exception as e:
    print(str(e))

try:
    print(matrix_divided(matrix, float('inf')))
except Exception as e:
    print(str(e))

try:
    print(matrix_divided())
except Exception as e:
    print(str(e))
