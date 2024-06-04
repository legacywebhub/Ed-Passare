x = float(input('Enter number:'))

def factorial(n):
    # Base case: factorial of 1 is 1
    if n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Dispaying output
print("Result: ", factorial(x))
