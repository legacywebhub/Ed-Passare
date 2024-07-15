name1 = "Annette"
name2 = "Mr Paulson"
greeting = "Hello"
annette_age = 15

# String concatenation
full_greeting = greeting + " " + name1 + ". My age is " + str(annette_age)
# String literal
full_greeting2 = f"{greeting} {name1} and {name2}. Hope you are having a great day"
# Special Characters
quote = '\'Always remember you are unique\''
# String methods
quote_uppercase = quote.upper() # Uppercase
quote_lowercase = quote.lower() # Lowercase
quote_length = len(quote) # Length of a string
age = str(annette_age)  # Convert to string


print("Hello ", name1, name2)