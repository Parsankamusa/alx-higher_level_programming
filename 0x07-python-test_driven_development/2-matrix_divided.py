#!/usr/bin/python3
"""
Module 2-matrix_divided
Contain one mthod that divided the element of
The same size of int or float matrix
Return the dividened number rouneded to two decimal place
"""


def matrix_divided(matrix, div):
        """Return new matrix with dividened"""
        message = "matrix must be a matrix (list of lists) of integers/floats"
        message_one = "Each row of the matrix must have the same size"
        if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
            raise TypeError(message)
        for rows in matrix:
            if type(rows) is not list:
                raise TypeError(message)
            for i in rows:
                if type(i) is not int and type(i) is not float:
                    raise TypeError(message)
                samelen = len(matrix[0])
                for row in matrix:
                    if samelen != len(row):
                        raise TypeError(message_one)
                    if type(div) is not int and type(div) is not float:
                        raise TypeError("div must be a number")
                    if div == 0:
                        raise ZeroDivisionError("division by zero")
                    return [[round(i / div, 2) for i in rows] for rows in matrix]
