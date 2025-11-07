import numpy as np

# defining the operators in NumPy
def get_operator(operator_name: str):
    operators = np.array(['+', '-', '*', '/', '%', '**', '//', 'sqrt'])
    try:
        index = np.where(operators == operator_name)[0][0]
        return operators[index]
    except IndexError:
        return "Invalid operator"
    


def evaluationProcess(operator, num1, num2=None):
    if operator == '+':
        return np.add(num1, num2)
    elif operator == '-':
        return np.subtract(num1, num2)
    elif operator == '*':
        return np.multiply(num1, num2)
    elif operator == '/':
        return np.divide(num1, num2)
    elif operator == '%':
        return np.mod(num1, num2)
    elif operator == '**':
        return np.power(num1, num2)
    elif operator == '//':
        return np.floor_divide(num1, num2)
    elif operator == 'sqrt':
        return np.sqrt(num1)  # only one argument
    else:
        return "Invalid operator"


if __name__ == "__main__":
    operator = get_operator('sqrt')
    print("Operator:", operator)

    result = evaluationProcess(operator, 16)
    print("Result:", result)
