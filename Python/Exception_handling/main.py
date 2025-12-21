# 1️⃣ What is an Exception?

# An exception is an error that occurs while your program is running (not while writing it).
# When Python sees an error — like dividing by zero or accessing something that doesn’t exist — it stops the program unless you handle it.

    # Example ⛔️

    # a = 10
    # b = 0
    # print(a / b)


    # Output:

    # ZeroDivisionError: division by zero


# ➡️ The program crashes because Python doesn’t know what to do.

# 🧩 2️⃣ What is Exception Handling?

# Exception handling means:
# You tell Python what to do when an error happens — so your program doesn’t crash.

# You do this using the try, except, else, and finally blocks.

    # ⚙️ 3️⃣ Basic Structure
    # try:
    #     # code that might cause an error
    #     x = 10 / 0
    # except:
    #     # what to do if an error happens
    #     print("Something went wrong!")


    # Output:

    # Something went wrong!


    # ✅ The program doesn’t crash anymore.

# 🎯 4️⃣ Catching Specific Errors

# You can catch specific types of exceptions (recommended way):

    # try:
    #     num = int(input("Enter a number: "))
    #     print(10 / num)
    # except ValueError:
    #     print("That’s not a valid number.")
    # except ZeroDivisionError:
    #     print("You can’t divide by zero.")


    # So if the user types:

    # "abc" → it shows That’s not a valid number.

    # 0 → it shows You can’t divide by zero.

    # 🔁 5️⃣ Using else and finally

    # else → runs if no error occurs

    # finally → runs no matter what happens (even if there’s an error)

    # Example:

    # try:
    #     x = 10 / 2
    # except ZeroDivisionError:
    #     print("Error: division by zero")
    # else:
    #     print("No error! Division successful.")
    # finally:
    #     print("This will always run.")


    # Output:

    # No error! Division successful.
    # This will always run.

    # 💡 6️⃣ Why it’s important

    # Exception handling helps you:

    # Prevent program crashes

    # Show friendly error messages

    # Handle invalid input safely

    # Continue running the rest of the code



try:
    number : int
    number = int(input("Enter a number: "))
    print(f"The number is: {number}")

except ValueError:
    print("That's not a valid number.")

finally:
    print("This will always run.")