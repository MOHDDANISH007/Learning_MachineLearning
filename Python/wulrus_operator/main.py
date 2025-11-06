# 🦭 What is the Walrus Operator (:=)?

# The walrus operator (:=) is used to assign a value to a variable inside an expression
#  — while also using that value immediately.

# It was introduced in Python 3.8.

# 💡 Normal way (before Python 3.8)


# data = input("Enter your name: ")
# if len(data) > 0:
#     print("Hello,", data)


# 🦭 Using the walrus operator

# With :=, you can assign and check at the same time:


if (data := int(input("Enter the number please! "))) > 0:
    print("Hello data is greater then 0 ,", data)
else:
    print("Hello data is less then 0 ,", data)


while len(name := input("Enter your name: ")) > 5:
    print("Hello,", name)
    break



