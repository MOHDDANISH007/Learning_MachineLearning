from module import get_operator, evaluationProcess
import os

if __name__ == "__main__":
    while True:
        # take user input
        List = input("Please enter the expression and give a space between the operands (e.g. 5 + 3): ").split(" ")
        user_operator = List[1]
        operator = get_operator(user_operator)
        num1 = int(List[0])
        
        # handle single operand operators like 'sqrt'
        if len(List) == 2:  # e.g., "9 sqrt"
            num2 = None
        else:
            num2 = int(List[2])

        # evaluate and prepare result
        result = evaluationProcess(operator, num1, num2)
        expression = f"{num1} {user_operator} {num2 if num2 is not None else ''} = {result}"

        # write result to file
        with open("result.txt", "a") as file:
            file.write(expression + "\n")

        # read and display file content
        with open("result.txt", "r") as f:
            print("\n📄 Read File:\n" + f.read())

        # ask user if they want to perform another operation
        again = input("Do you want to perform another operation? (yes/no): ").lower()
        if again != "yes":
            break  # exit the loop if user says no

    # ask if user wants to delete file
    delete_after_execution = input("Do you want to delete the file after execution? (yes/no): ").lower()
    if delete_after_execution == "yes":
        os.remove("result.txt")
        print("🗑️ Your file has been deleted.")
    else:
        print("✅ Your results are saved in 'result.txt'.")
