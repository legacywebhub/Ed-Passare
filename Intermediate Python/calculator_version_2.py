add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Cannot divide by zero"
modulo = lambda x, y: x % y if y != 0 else "Cannot divide by zero"

# Prompt user for the first number
while True:
    try:
        x = float(input('Enter a number: '))
        break  # Exit loop if input is successfully converted to float
    except ValueError:
        print("Please enter a valid number.")

# Prompt user for the operand
allowed_operands = ['+', '-', '*', '/', '%']
operand = input('Enter an operand (+, -, *, /, %): ')
while operand not in allowed_operands:
    print("Invalid operand. Please enter one of: +, -, *, /, %")
    operand = input('Enter an operand (+, -, *, /, %): ')

# Prompt user for the second number
while True:
    try:
        y = float(input('Enter a second number: '))
        break  # Exit loop if input is successfully converted to float
    except ValueError:
        print("Please enter a valid number.")

# Perform calculation based on the operand
if operand == '+':
    operation = "Addition"
    result = add(x, y)
elif operand == '-':
    operation = "Subtraction"
    result = subtract(x, y)
elif operand == '*':
    operation = "Multipication"
    result = multiply(x, y)
elif operand == '/':
    operation = "Division"
    result = divide(x, y)
elif operand == '%':
    operation = "Modulo"
    result = modulo(x, y)

# Display results
print(operation, " Result:", result)