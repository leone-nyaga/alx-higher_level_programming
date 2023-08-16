#!/usr/bin/python3
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_row = [x ** 2 for x in row]
        squared_matrix.append(squared_row)
    return squared_matrix
