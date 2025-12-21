import numpy as np

# give the shape(shape, value)  
filledWithZeros = np.zeros((2, 3));
filledWithOnes = np.ones((2, 3));
filledWithSpecific_Value = np.full((2, 3), 10);

print(f"Filled With Zeros: \n {filledWithZeros}")
print(f"Filled With Ones: \n {filledWithOnes}")
print(f"Filled With Specific Value: \n {filledWithSpecific_Value}")


list = ["Mohammad Danish", "Mohmmad Kashif", "Muhammad Ali"]

listArray = np.array(list)
print(f"List Array: \n {listArray}")
print(f"type of listArray: \n {type(listArray)}")


# arrange the sequence number of the array
# arrange(start, stop, step)
arrangedArray = np.arange(0, 10, 2);
print(f"Arranged Array: \n {arrangedArray}")


# creating an Identity Matrix
identityMatrix = np.eye(3);
print(f"Identity Matrix: \n {identityMatrix}")