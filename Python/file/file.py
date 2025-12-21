# File Handling


# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists


# Open and read demo.txt
f = open("demo.txt")
print(f"Read File: \n {f.read()}")
f.close()

# Open and read main.py using raw string
anotherFile = open(r"C:\Users\mohdd\OneDrive\Documents\Desktop\MachineLearning\Numpy\advanced\main.py", encoding="utf-8")
print(f"Advanced NumPy: \n {anotherFile.read()}")
anotherFile.close()



with open(r"C:\Users\mohdd\OneDrive\Documents\Desktop\MachineLearning\Numpy\HandlingMissingValue\main.py", encoding="utf-8") as f:
    print(f"Handling Missing Value: \n {f.read()}")
    f.close()


# append the data into demofile.txt

with open("demo.txt", "a") as f:
    f.write("\nNow the file has more content!");
    f.close();

with open("demo.txt", "r") as f:
    print(f"Read File: \n {f.read()}")
    f.close()


# write mode

with open("demofile.txt", "w") as f:
    f.write("\nOops I did it again!");
    f.close();

with open("demofile.txt", "r") as f:
    print(f"Read File: \n {f.read()}")
    f.close()