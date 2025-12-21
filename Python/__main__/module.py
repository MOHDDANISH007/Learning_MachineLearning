# 🧩 Meaning in simple words

# if __name__ == "__main__":
# 👉 means: “Run this code only when the file is executed directly, not when it’s imported.”


# 🔍 Example to match your explanation

# greet.py

    # def greeting(name):
    #     print(f"Hello, {name}!")

    # if __name__ == "__main__":
    #     # This is just for testing
    #     greeting("Danish")   # static test value


# Now, if someone imports it in another file 👇

# main.py

    # import greet

    # greet.greeting("Ayesha")  # They can pass any name dynamically

# 🧠 What happens

    # When you run python greet.py →
    # Output: Hello, Danish! ✅ (test code runs)

    # When you run python main.py →
    # Output: Hello, Ayesha! ✅ (test code does not run)

# 🎯 Purpose

    # Exactly as you said:

    # When another person imports the file, they only want to use the function, not run your test code or static examples.

    # That’s why we keep test/example code inside:

    # if __name__ == "__main__":
    #     # This is just for testing
    #     greeting("Danish")




def greeting(name:str)->None:
    print(f"Hello, {name}!")


def addingTwoNumber(number1 : int, number2 : int)->int:
    return number1 + number2    

if __name__ == "__main__":
    # This is just for testing
    greeting("Danish")

    print(addingTwoNumber(1,2))