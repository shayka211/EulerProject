

# the idea is to go from down of the matrix, each triangle take the maximum option
# this way we reduce the matrix to minus row with the same problem, until we stay with only one function

import numpy as np


def get_triangle(triangle_filename):
    """Return a list of lists containing rows of the triangle."""
    triangle = open(triangle_filename).read().split('\n')
    triangle = [[int(number) for number in row.split()] for row in triangle]
    return triangle


def maximum_path_sum(matrix):
    for j in range(len(matrix)-1):
        count = 0
        for i in range(len(matrix[len(matrix)-j-2])):
            matrix[len(matrix)-j-2][i] += max(matrix[len(matrix)-j-1][count], matrix[len(matrix)-j-1][count + 1])
            count += 1
    return matrix[0][0]


def problem18():
    matrix = get_triangle("triangle.txt")
    print("the solution is ", maximum_path_sum(matrix))


if __name__ == "__main__":
    problem18()
    # combine_rows(get_triangle("triangle.txt"))
