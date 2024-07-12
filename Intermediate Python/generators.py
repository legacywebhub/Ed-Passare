# GENERATORS

'''
Generators in Python are similar to lists and tuples, but with a crucial difference: they generate values on-the-fly, one at a time, instead of storing them all in memory at once. This makes generators very memory efficient, especially when dealing with large datasets or infinite sequences.

Generators are useful when you have lots of things to work with but you don’t need them all at once. They save space and can be faster!

Syntax: Generators are created using functions with yield statements. When a function with yield is called, it returns a generator object without actually executing the function. Each yield statement pauses the function and saves its state, allowing it to resume where it left off when called again.
'''

# Creating a generator to give us numbers
def number_generator():
    yield 1
    yield 2
    yield 3

# Using the generator
numbers = number_generator()

# Getting the next number
print(next(numbers))  # Prints: 1

# Getting the next number again
print(next(numbers))  # Prints: 2

# And the next one
print(next(numbers))  # Prints: 3

