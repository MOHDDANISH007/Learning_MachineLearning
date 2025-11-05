import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = np.vstack((arr1, arr2))
print(f"Vertical Stack: \n {result}")



result = np.hstack((arr1, arr2))
print(f"Horizontal Stack: \n {result}")


arr2_D = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

arr3_D = np.array([
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
])


result = np.vstack((arr2_D, arr3_D))
print(f"Vertical Stack: \n {result}")

result = np.hstack((arr2_D, arr3_D))
print(f"Horizontal Stack: \n {result}")