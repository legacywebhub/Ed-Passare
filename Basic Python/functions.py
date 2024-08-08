name2 = "Mr. Paulson"   # Global variable


def say_hello(age, name = "Mr Joseph"):
    return f"Hello {name}, I am {age} years old"


print(say_hello(25, "Paulson"))
print(say_hello(12, "Annette"))
print(say_hello(30))


x = int(input("Enter first number: "))
operation = input("Enter an operand(+, -, *, /): ")
y = int(input("Enter second number: "))

def addNumbers(a, b):
    return a + b

def subtractNumbers(a, b):
    return a - b

def multiplyNumbers(a, b):
    return a * b

def divideNumbers(a, b):
    return a / b

if (operation == "+"):
    print(addNumbers(x, y))
elif (operation == "-"):
    print(subtractNumbers(x, y))
elif (operation == "*"):
    print(multiplyNumbers(x, y))
elif (operation == "/"):
    print(divideNumbers(x, y))
else:
    print("operation not valid")