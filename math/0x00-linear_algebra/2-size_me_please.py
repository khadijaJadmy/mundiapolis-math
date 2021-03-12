#!/usr/bin/env python3
def matrix_shape(matrix):
    val = len(matrix)
    val2 = val3 = 0
    for x in matrix:
        if(type(x) != int):
            for y in matrix[matrix.index(x)]:
                val2 = len(matrix[matrix.index(x)])
                if(type(y) != int):
                    val3 = len(y)
                else:
                    return [val, val2]
        else:
            return [val]

    return [val, val2, val3]


mat1 = [[1, 2], [3, 4]]
print(matrix_shape(mat1))
mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
print(matrix_shape(mat2))
