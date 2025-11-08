import numpy as np


# np_1d = np.array([1, 2, 3])
# print(np_1d)

# print(f"type of np: {type(np_1d)}")


# # multi-dimensional array

# np_2d = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# print(f"2d array: \n {np_2d}")


# np_3d = np.array([
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ],
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
# ])

# print(f"3d array: \n {np_3d}")



# zero , one and full method in numpy

zeroArray = np.zeros((2, 3))

print(f"Zero Array: \n {zeroArray}")

onesArray = np.ones((2, 3))

print(f"One Array: \n {onesArray}")

fullArray = np.full((2, 3), 10)

print(f"Full Array: \n {fullArray}")    

# arange method

arrangedArray = np.arange(0, 10, 2)

print(f"Arranged Array: \n {arrangedArray}")


# identity matrix

identityMatrix = np.eye(3)

print(f"Identity Matrix: \n {identityMatrix}")


# random element in the 2 X 3 matrix

randomArray = np.random.randint(0, 10, (3,3))
print(f"Random Array: \n {randomArray}")


reshapeTheArrangeArray = np.arange(1, 17, 1).reshape(4, 4)

print(f"Reshape Array: \n {reshapeTheArrangeArray}")


# shape of the array 

print(f"Shape of Array: \n {reshapeTheArrangeArray.shape}")


# Tells how many dimensions the array has, 2 → because it’s a 2D array

print(f"Number of Dimension: \n {reshapeTheArrangeArray.ndim}")

# Data type

print(f"Data Type: \n {reshapeTheArrangeArray.dtype}")


# flatten() Convert to 1D arr.flatten()


flattenArray = reshapeTheArrangeArray.flatten()

print(f"Flatten Array: \n {flattenArray}")


# minimum and maximum value in the multi dimensional array


print(f"Minimum Value: \n {np.min(reshapeTheArrangeArray)}")
print(f"Maximum Value: \n {np.max(reshapeTheArrangeArray)}")

# sum of all elements in the array
print(f"Sum of all elements in the array : \n {np.sum(reshapeTheArrangeArray)}")


# sort all the elements in the random array
print(f"Sort all the elements in the random array: \n {np.sort(randomArray)}")

#  i want only limited number of elements

print(f"Limited number of elements: \n {np.clip(reshapeTheArrangeArray, 0 , 10)}")
print(f"Limited number of elements: \n {np.clip(flattenArray, 0 , 10)}")