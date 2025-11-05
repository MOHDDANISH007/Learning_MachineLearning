import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(f"Concatenation of Array: \n {np.concatenate((arr1, arr2))}") 

# # Addition
# print(f"Addition of Array: \n {arr1 + arr2}")

# # Multiplication
# print(f"Multiplication of Array: \n {arr1 * arr2}")

# # Subtraction
# print(f"Subtraction of Array: \n {arr1 - arr2}")

# # Dot Product
# print(f"Dot Product of Array: \n {arr1.dot(arr2)}")

# # Cross Product
# print(f"Cross Product of Array: \n {np.cross(arr1, arr2)}")

# # Power
# print(f"Power of Array: \n {arr1 ** arr2}")

# # Modulus
# print(f"Modulus of Array: \n {arr1 % arr2}")

# # Floor
# print(f"Floor of Array: \n {arr1 // arr2}")

# # Boolean
# print(f"Boolean of Array: \n {arr1 > arr2}")

# # Boolean
# print(f"Boolean of Array: \n {arr1 < arr2}")




# using numpy to do all this operation

print(np.add(arr1, arr2))
print(np.subtract(arr1, arr2))
print(np.multiply(arr1, arr2))
print(np.dot(arr1, arr2))
print(np.cross(arr1, arr2))
print(np.power(arr1, arr2))
print(np.mod(arr1, arr2))
print(np.floor_divide(arr1, arr2))


# Common Statistical Functions

print(f"Mean of Array: \n {np.mean(arr1)}")

print(f"Median of Array: \n {np.median(arr1)}")

print(f"Standard Deviation of Array: \n {np.std(arr1)}")

print(f"Variance of Array: \n {np.var(arr1)}")

print(f"Minimum of Array: \n {np.min(arr1)}")

print(f"Maximum of Array: \n {np.max(arr1)}")



# Slicing arrays
# Slicing in python means taking elements from one given index to another given index.

# We pass slice instead of index like this: [start:end].

# We can also define the step, like this: [start:end:step].

# If we don't pass start its considered 0

# If we don't pass end its considered length of array in that dimension

# If we don't pass step its considered 1



arr3 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])



print(f"Slicing of Array: \n {arr3[0:2, 0:3]}")


# filtering in numpy

arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(f"Filtering of Array: \n {arr4[arr4 > 5]}")


# get the bool result like [True, True, False, False, False, False, False, False, False, False]
# filterEvenNumber = arr4 % 2 == 0
# print(f"Filtering of Array: \n {filterEvenNumber}")


filterEvenNumber = arr4[arr4 % 2 == 0]
print(f"Filtering of Array: \n {filterEvenNumber}")

arr2D = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(f"Filtering of Array: \n {arr2D[arr2D > 5]}") 


# Reshaping into the array by using numpy

arr5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(f"Reshaping of Array: \n {arr5.reshape(2, 5)}")


arr6_2D = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(f"Reshaping of Array: \n {arr6_2D.reshape(1, 9)}")




# difference between in ravel and flatten

# arr7 = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# print(f"Ravel of Array: \n {arr7.ravel()}")
# print(f"Flatten of Array: \n {arr7.flatten()}")


# f = arr7.flatten()
# f[0] = 99
# print(arr7)  # original array stays same


# r = arr7.ravel()
# r[0] = 99
# print(arr7)  # original array also changes