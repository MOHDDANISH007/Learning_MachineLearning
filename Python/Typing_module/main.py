# 💡 But what is the typing module?

# Python has a built-in typing module that allows you to specify variable types manually (optional).
# This is called Type Hinting or Static Typing.

# It helps make your code:

# Easier to read 🧐

# Easier to debug ✅

# Safer for large projects (like ML, APIs, etc.)


# 🧩 Example: Without typing


# def add(a, b):
#     return a + b

# print(add(5, 10))      # Works
# print(add("Hi", "Yo")) # Also works, but maybe not what you want



# ⚙️ Example: With typing


# from typing import List

# def add(a: int, b: int) -> int:
#     return a + b

# print(add(5, 10))      # ✅ Works
# print(add("Hi", "Yo")) # ⚠️ Error (type checker warning)


# | Type Hint          | Meaning              | Example                                    |
# | ------------------ | -------------------- | ------------------------------------------ |
# | `int`              | Integer              | `age: int = 25`                            |
# | `float`            | Decimal number       | `pi: float = 3.14`                         |
# | `str`              | String               | `name: str = "Danish"`                     |
# | `bool`             | Boolean              | `is_valid: bool = True`                    |
# | `List[int]`        | List of integers     | `nums: List[int] = [1,2,3]`                |
# | `Tuple[str, int]`  | Pair of string & int | `person: Tuple[str, int] = ("Ali", 20)`    |
# | `Dict[str, float]` | Dictionary           | `marks: Dict[str, float] = {"Math": 90.5}` |
# | `Any`              | Any type allowed     | `value: Any = 10 or "hi"`                  |
# | `Optional[int]`    | int or None          | `age: Optional[int] = None`                |




# but why it is come up because already python data types can hold the multiple values like list , tuple and dictinary


# 🧠 1️⃣ Problem Before Typing

# Python is a dynamically typed language — meaning you don’t need to declare variable types.


# x = 10
# x = "Hello"



# This is valid in Python. But in big projects or machine learning models, this flexibility can cause bugs because:

# You might accidentally pass a string where a number is expected.

# You might return wrong types from functions.

# Python wouldn’t warn you until runtime (when the code actually runs).


# 💡 2️⃣ Typing Solves This

# The typing module allows you to hint what types of data are expected.
# It doesn’t change how Python runs — it just helps tools (like editors or linters) detect mistakes early.

# Example:


# def add(a: int, b: int) -> int:
#     return a + b


# ✅ Correct usage:

# add(5, 10)


# ❌ Incorrect usage (warning in IDE):

# add("5", 10)


# ⚙️ 3️⃣ Works with Lists, Dicts, etc.

# Typing also helps describe complex data types:


# from typing import List, Dict, Tuple

# marks: List[int] = [85, 90, 78]
# student: Dict[str, int] = {"Danish": 90, "Amit": 85}
# position: Tuple[int, int] = (10, 20)



from typing import List, Dict, Tuple

booleanArray : List[bool] = []

i : int = 0;

while i < 10:
    booleanArray.append((data := (i%2 == 0)) == True)
    i += 1

print(f"Boolean Array: {booleanArray}")

print(f"type of booleanArray and i: {type(booleanArray)} and {type(i)}")


# giving me the warning of type hinting

# i = "string"

# print(f"type of booleanArray and i: {type(booleanArray)} and {type(i)}")


def addTwoNumber(a : int, b:int) ->int:
    return a + b

print(f"addTwoNumber: {addTwoNumber(5, 10)}")