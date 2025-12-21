# 💥 1️⃣ What Does "Raising an Error" Mean?

    # Normally, Python automatically raises
    #  (shows) an error when something goes wrong,
    # like dividing by zero or using a wrong type.

    # But sometimes you want to raise an error on purpose —
    # for example, when a user gives wrong input or something invalid happens in your program.

    # That’s when we use the raise keyword.

# ⚙️ 2️⃣ Syntax

# raise ErrorType("custom error message")


# Example 1️⃣: Simple Custom Error

    # age = int(input("Enter your age: "))

    # if age < 0:
    #     raise ValueError("Age cannot be negative.")
    # else:
    #     print("Valid age:", age)


# 🧠 If the user types -5, output will be:
    # ValueError: Age cannot be negative.

# Example 2️⃣: Raising Different Errors

    # name = input("Enter your name: ")

    # if not name:
    #     raise TypeError("Name cannot be empty!")


# Output:

    # TypeError : Name cannot be empty!


# 🧩 3️⃣ Common Types of Errors (Exceptions) in Python

# Here are the most common ones you’ll face in real projects and interviews 👇

# | Error Type          | Description               | Example               |
# | ------------------- | ------------------------- | --------------------- |
# | `ValueError`        | Wrong value given         | `int("abc")`          |
# | `TypeError`         | Wrong data type           | `"5" + 3`             |
# | `IndexError`        | Accessing invalid index   | `mylist[10]`          |
# | `KeyError`          | Missing key in dictionary | `mydict["xyz"]`       |
# | `ZeroDivisionError` | Dividing by zero          | `5 / 0`               |
# | `NameError`         | Variable not defined      | `print(x)`            |
# | `FileNotFoundError` | File not found            | `open("abc.txt")`     |
# | `AttributeError`    | Invalid attribute access  | `"hello".append(2)`   |
# | `ImportError`       | Module not found          | `import not_a_module` |
# | `AssertionError`    | Assertion fails           | `assert 5 > 10`       |




# 🚀 4️⃣ Custom Exceptions (Your Own Error Class)

# You can even create your own custom error by using classes.

# Example 👇

    # class AgeTooSmallError(Exception):
    #     pass

    # age = int(input("Enter your age: "))

    # if age < 18:
    #     raise AgeTooSmallError("Age must be at least 18!")


# Output:
    # AgeTooSmallError: Age must be at least 18!


# 🧩 1️⃣ Basic Custom Error Example

# You can create your own error by defining a new class that inherits from Exception.


# class NegativeNumberError(Exception):
#     pass

# num = int(input("Enter a positive number: "))

# if num < 0:
#     raise NegativeNumberError("Number cannot be negative!")
# else:
#     print("You entered:", num)


# 🧠 If user enters -5 →

# Output: NegativeNumberError: Number cannot be negative!


# 📘 2️⃣ Custom Error for Age Validation

    # class InvalidAgeError(Exception):
    #     pass

    # def check_age(age):
    #     if age < 0:
    #         raise InvalidAgeError("Age cannot be negative.")
    #     elif age < 18:
    #         raise InvalidAgeError("You must be at least 18 years old.")
    #     else:
    #         print("Access granted!")

    # try:
    #     check_age(15)
    # except InvalidAgeError as e:
        # print("Error:", e)

# Output : Error: You must be at least 18 years old.


age : int  = int(input("Enter your age: "))

try:
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise ValueError("You must be at least 18 years old.")
    else:
        print("Access granted!")

except ValueError as e:
    print("Error:", e)

finally:
    print("Program completed.")



class AgeTooSmallerError(Exception):
    pass


try:
    if age < 0:
        raise AgeTooSmallerError("Age cannot be negative.")
    elif age < 18:
        raise AgeTooSmallerError("You must be at least 18 years old.")
    else:
        print("Access granted!")

except AgeTooSmallerError as e:
    print("Error:", e)

finally:
    print("Program completed.")