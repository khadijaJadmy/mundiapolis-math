
def cat_arrays(arr1, arr2):
    arr=[*arr1,*arr2]
    return arr

arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8]
print(cat_arrays(arr1, arr2))
print(arr1)
print(arr2)