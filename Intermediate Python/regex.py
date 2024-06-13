# Importing the regular expressions library
import re 

footballers = [ # names of footballers
    "Christaino Ronaldo",
    "Lionel Messi",
    "Mohammed Sallah",
    "Kylian Mbappe",
    "Vinius Junior",
    "Delima Ronaldo",
    "Ronaldinho",
]

# Test for first name and last name
pattern = "^\w+ \w+$"
for name in footballers:
    result = re.search(pattern, name)
    if result:
        print(name)


# Searching example
pattern = "\bC\w*"  # Pattern to find one or more digits
text = "There are 123 apples and 456 oranges. Please add more apples because apples sell more"
matches = re.findall(pattern, text)
print(matches)  # Output: ['123', '456']


# Replacing example
pattern = r"apple"  # Pattern to find the word "apple"
replacement = "banana"
new_text = re.sub(pattern, replacement, text)
print(new_text)  # Output: "There are 123 bananas and 456 oranges. Please add more bananas because apples sell more"