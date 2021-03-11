
def add_matrices2D(mat1, mat2):
    if( len(mat1[0])==len(mat2[0])):
        result = [[mat1[i][j] + mat2[i][j]  for j in range(len(mat1[0]))] for i in range(len(mat1))]
        return result
    else:
        return None

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(add_matrices2D(mat1, mat2))
print(mat1)
print(mat2)
print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))