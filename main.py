def calculator():
    operations = []  # List to store operations

    print("Enter an Operation (or 'exit' to quit or 'history' to show operations history): ")
    while True:
        expression = input()
        if expression.lower() == 'exit':
            break
        elif expression.lower() == 'history':
            print("\nHistory of Operations:")
            for op in operations:
                print(op)
        else:
            result = evaluate_expression(expression)
            operations.append(f"{expression} = {result}")
            print(f"{expression} = {result}")


def evaluate_expression(expression):
    # Split the expression into numbers and operators
    numbers = []
    operators = []
    current_number = ''
    for char in expression:
        if char.isdigit() or char == '.':
            current_number += char
        else:
            if current_number:
                numbers.append(float(current_number))
                current_number = ''
            if char in ['+', '-', '*', '/']:
                operators.append(char)

    if current_number:
        numbers.append(float(current_number))

    # Perform the operations with priority
    i = 0
    while i < len(operators):
        if operators[i] in ['*', '/']:
            if operators[i] == '*':
                result = numbers[i] * numbers[i + 1]
            else:
                result = numbers[i] / numbers[i + 1]
            # Replace the operands and operator with the result
            numbers[i] = result
            numbers.pop(i + 1)
            operators.pop(i)
        else:
            i += 1

    # Perform the remaining operations
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i - 1] == '+':
            result += numbers[i]
        elif operators[i - 1] == '-':
            result -= numbers[i]

    return result


calculator()
