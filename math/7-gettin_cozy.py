import numpy as np

def cat_matrices2D(mat1, mat2, axis=0):
    #a=np.array(mat1)
    #b=np.array(mat2)
    M=np.concatenate((mat1,mat2),axis)
    return M


mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6]]
mat3 = [[7], [8]]
mat4 = cat_matrices2D(mat1, mat2)
mat5 = cat_matrices2D(mat1, mat3, axis=1)
print(mat4)
print(mat5)
mat1[0] = [9, 10]
mat1[1].append(5)
print(mat1)
print(mat4)
print(mat5)