def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Prompt user for the first number
x = float(input('Enter a number: '))
# Prompt user for an operand
operand = input('Enter an operand(+, -): ')
# Prompt user for the first number
y = float(input('Enter a second number: '))


if operand == '+':
    print(x + y)
elif operand == '-':
    print(x - y)
else:
    print('You entered a wrong operand')