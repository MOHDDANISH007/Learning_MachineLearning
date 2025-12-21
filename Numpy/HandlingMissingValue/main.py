import numpy as np

# NOte : We can't compare missing value with any other value

# Example : 1️⃣ Check missing value

array = np.array([10, 20, np.nan, 40, 50])
array2_D = np.array([
    [1, 2, 3],
    [4, np.nan, 6],
    [7, 8, 9]
])


print(f"Original Array: \n {array}")

# check wheather it has any missing value or not
print(f"Missing Value: \n {np.isnan(array)}")





# 2️⃣ Remove missing values

clean_arr = array[~np.isnan(array)]
print(f"Clean Array: \n {clean_arr}")


# remove missing value from 2D array
clean_arr2_D = array2_D[~np.isnan(array2_D)]
print(f"Clean 2D Array: \n {clean_arr2_D}")



# 3️⃣ Replace (fill) missing values

filled_arr = np.nan_to_num(array, nan = 15)
print(f"Filled Array: \n {filled_arr}")



filled_arr2_D = np.nan_to_num(array2_D, nan = 5)
print(f"Filled 2D Array: \n {filled_arr2_D}")



# finding the infinite value in the array

array3 = np.array([1, np.inf, 3, np.nan, 5])
print(f"Original Array: \n {array3}")

print(f"Missing Value: \n {np.isinf(array3)}")


replaced_arr3 = np.nan_to_num(array3, nan = 15, posinf = 20, neginf = 10)
print(f"Replaced Array: \n {replaced_arr3}")