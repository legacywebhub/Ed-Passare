### Debugging Techniques

'''
What is Debugging?
- Debugging is the process of finding and fixing errors (bugs) in your code.
'''

# 3 Common Debugging Techniques:

'''
1. Print Statements

   - Use print statements to display the values of variables at different points in your code.
   - Example:
'''
     
def add_numbers(a, b):
    print("a:", a)  # Print the value of a
    print("b:", b)  # Print the value of b
    result = a + b
    print("result:", result)  # Print the result
    return result

add_numbers(2, 3)
     

'''
2. Using an IDE or Debugger
   
    - Use an Integrated Development Environment (IDE) with built-in debugging tools like setting breakpoints, stepping through code, and inspecting variables.
'''

'''
3. Exception Handling

   - Use try-except blocks to catch and handle errors.
   - Example:
'''

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

'''
4. Code Reviews

   - Have someone else review your code to catch errors you might have missed.
'''


### Unit Testing

'''
What is Unit Testing?

- Unit testing is a way to test individual units or components of your code to ensure they work as expected.

Why is Unit Testing Important?

- It helps you catch bugs early.
- It makes your code more reliable.
- It makes it easier to refactor your code.

Example Using the `unittest` Module in Python:
'''


import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add_numbers(2, -3), -1)

if __name__ == '__main__':
    unittest.main()

'''
- The code above defines a function `add_numbers` and a test class `TestAddNumbers` with three test cases.
'''

### Test-Driven Development (TDD)

'''
What is TDD?

- Test-Driven Development (TDD) is a software development approach where you write tests before writing the actual code. 
The process follows these steps:

  1. Write a test for a new feature or function.
  2. Run the test and see it fail (since the function isn't written yet).
  3. Write the minimum amount of code to make the test pass.
  4. Refactor the code if needed, and ensure the test still passes.
  5. Repeat for each new feature or function.

Example of TDD:
'''

import unittest

def add_numbers(a, b):
    pass  # Function not implemented yet

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

if __name__ == '__main__':
    unittest.main()

'''
2. Run the Test and See it Fail:

   - When you run this test, it will fail because `add_numbers` isn't implemented yet.

   
3. Write the Code to Make the Test Pass:
   
   def add_numbers(a, b):
       return a + b
   

4. Run the Test and See it Pass:

   - Now when you run the test, it should pass.

5. Refactor if Needed:

   - If the code is simple, refactoring might not be necessary. But as your code grows, you may need to clean it up while ensuring the tests still pass.
'''


### Summary

'''
- Debugging** helps you find and fix errors in your code.

- Unit Testing** ensures individual parts of your code work correctly.

- Test-Driven Development (TDD)** involves writing tests before writing the code, helping you write cleaner and more reliable code.
'''
