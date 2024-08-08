# Conditional Statements in Python

Conditional statements are statements that help the computer make decisions. A condition can either be So a condition/conditional expression can either return `True` or `False` only after evaluated.

```python
# Define variables
favourite_superhero = "Aquaman"
universe = "DC"

# Basic Conditional Statement
if (favourite_superhero == "Superman" or universe == "DC"):
    print("You are a fan of Superman and his universe is DC")
elif (favourite_superhero == "Thor" and universe == "Marvel"):
    print("Man.. you are a marvel fan")
elif (favourite_superhero == "Hulk"):
    print("Hulk smasssshhhhhh")
else:
    print("You have no favourite superhero")

# Comparison Operators
'''
    ==   Equal to
    <=   Less than or equal to
    >=   Greater than or equal to
    !=   Not equal to
    >    Greater than
    <    Less than
'''

# Logical Operators
if (favourite_superhero == "Superman" and universe == "DC"):
    print("You are a fan of Superman in the DC universe")
if not (favourite_superhero == "Superman"):
    print("Your favourite superhero is not Superman")

# Nested Conditional Statements
if universe == "DC":
    if favourite_superhero == "Superman":
        print("You are a fan of Superman in the DC universe")
    elif favourite_superhero == "Aquaman":
        print("You like Aquaman from the DC universe")
    else:
        print("You are a DC fan, but not a fan of Superman or Aquaman")
else:
    print("You are not a DC universe fan")

# Ternary Conditional Operator
message = "DC fan" if universe == "DC" else "Not a DC fan"
print(message)