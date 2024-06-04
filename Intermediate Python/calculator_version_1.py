add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Cannot divide by zero"
modulos = lambda x, y: x % y if y != 0 else "Cannot divide by zero"

# Prompt user for the first number
x = float(input('Enter a number: '))
# Prompt user for the operand
operand = input('Enter an operand (+, -, *, /, %): ')
# Prompt user for the last number
y = float(input('Enter a second number: '))

# Perform calculation based on the operand
if operand == '+':
    print("Addition Result:", add(x, y))
elif operand == '-':
    print("Subtraction Result:", subtract(x, y))
elif operand == '*':
    print("Multipication Result:", multiply(x, y))
elif operand == '/':
    print("Division Result:", divide(x, y)) # Intentional error
elif operand == '%':
    print("Modulo Result:", modulos(x, y))
else:
    print("Invalid operand")