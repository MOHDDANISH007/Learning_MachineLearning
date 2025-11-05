import numpy as np


array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

array2 = np.array([1, 2, 3],[4, 5, 6],[7, 8, 9])


print(f"Original Array: \n {array}")


# Vectorization
print(f"Vectorization of Array: \n {array * 2}")


# Broadcasting
print(f"Broadcasting of Array: \n {array + array2}")