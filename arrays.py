import math
from functools import reduce

matrix_3x3 = [
    [1, 2, 3], 
    [4, 7, 9], 
    [8, 4, 2]
]


matrix_4x4 = [
    [1, 0, 0, 0], 
    [0, 1, 0, 0], 
    [0, 0, 1, 0], 
    [0, 0, 0, 1],
]
# find the trace of an n x n matrix


def trace(matrix):
    i = 0
    currentSum = 0
    for row in matrix: 
        currentSum += row[i]
        i += 1
    return currentSum


def antiTrace(matrix): 
    i = len(matrix) - 1
    currentSum = 0
    for row in matrix: 
        currentSum += row[i]
        i -= 1 
    return currentSum

print(trace(matrix_4x4))
print(antiTrace(matrix_4x4))

        