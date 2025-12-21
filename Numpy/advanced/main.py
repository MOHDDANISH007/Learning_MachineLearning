
# Advanced NumPy operations
import numpy as np

# -------------------------------
# INSERT METHOD IN NUMPY
# np.insert(array, index, values, axis)
# -------------------------------

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Original Array: \n{array}")

# Insert 0 at the beginning (index 0)
new_Array = np.insert(array, 0, 0)
print(f"New Array after Insert: \n{new_Array}")

# -------------------------------
# 2D Example
# -------------------------------

array2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"\nOriginal 2D Array: \n{array2}")

# Insert two new rows at index positions 2 and 3
new_Array2 = np.insert(
    array2,               # original array
    2,                    # index where to insert
    [[10, 11, 12], [13, 14, 15]],  # new rows
    axis=0                # 0 means row-wise
)
print(f"New Array2 after Insert (rows): \n{new_Array2}")

# -------------------------------
# APPEND METHOD IN NUMPY
# np.append(array, values, axis)
# -------------------------------

# Append a single element in 1D array
append_Array = np.append(array, 11)
print(f"\nAppend Array (1D): \n{append_Array}")

# Append a new row in 2D array
append_Array2 = np.append(array2, [[10, 11, 12]], axis=0)
print(f"\nAppend Array2 (add row): \n{append_Array2}")

# Append a new column in 2D array
append_Array3 = np.append(array2, [[10], [11], [12]], axis=1)
print(f"\nAppend Array3 (add column): \n{append_Array3}")




# np.concatenate() — Joining arrays together

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])


result = np.concatenate((arr1, arr2))
print(f"Concatenation of Array: \n {result}")



# 🔹 Example 2: Join 2D arrays (row-wise)


arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])

# axis=0 → join rows (top and bottom)
result = np.concatenate((arr3, arr4), axis=0)
print(f"Concatenation of 2D_Array: \n {result}")


# 🔹 Example 3: Join 2D arrays (column-wise)

result2 = np.concatenate((arr3, arr4), axis=1)
print(f"Concatenation of 2D_Array: \n {result2}")



# 🧹 2️⃣ Removing Elements/Rows/Columns in NumPy

# np.delete(array, index, axis)
# np.delete(array, indices, axis)


arr5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Delete the first element
deleted_Array = np.delete(arr5, 5)
print(f"Deleted Array: \n {deleted_Array}")


arr6 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

deleted_Array2 = np.delete(arr6, 2, axis=0)
print(f"Deleted Array2: \n {deleted_Array2}")


deleted_Array3 = np.delete(arr6, 1, axis=1)
print(f"Deleted Array3: \n {deleted_Array3}")