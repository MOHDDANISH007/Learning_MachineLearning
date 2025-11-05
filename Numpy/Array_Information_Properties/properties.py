import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# 1st shape
print(f"Shape: {arr.shape }")

# arr.ndim
print(f"Dimension: {arr.ndim}")

# arr.size

print(f"Size: {arr.size}")

# arr.dtype
print(f"Data Type: {arr.dtype}")

# arr.reshape()

# first i need to arrange the element of the array

arr2 = np.arange(1, 17)

print(f"Reshape: {arr2.reshape(4, 4)}")

flattenArray = arr2.flatten()
print(f"Flatten Array: {flattenArray}")

# astype

arr3 = np.array([
    "1", "2", "3" , "5"
])

print(f"Elements: {arr3}")
arr4 = arr3.astype(int)

# delete the last element
arr5 = np.delete(arr4, 3)
print(f"Delete: {arr5}")
# pusht the element in the last
arr5 = np.append(arr5, [4,5,6,7])
print(f"Append: {arr5}")

arr3 = arr5.astype(str);

