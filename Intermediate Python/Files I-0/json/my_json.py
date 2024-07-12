## What is JSON

'''
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write 
and easy for machines to parse and generate. It is commonly used for transmitting data in web applications.

Imagine you have a notebook where you write information in a very organized way using pairs. 
Each piece of information has a key (like a name) and a value (like the person's age). 
For example, if you write about your friends, you might have a key for each friend's name and a value for their age. 
This special notebook is like a JSON file.
'''

## 


import json

# Define the path to your JSON file
json_file_path = 'data/sample.json'

# Create sample JSON data
data = {
    "Friends": [
        {
            "Name": "Alice",
            "Age": 25,
            "FavoriteColor": "Red"
        },
        {
            "Name": "Bob",
            "Age": 30,
            "FavoriteColor": "Blue"
        }
    ]
}

# Writing the JSON data to a file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
print(f"JSON file written to {json_file_path}")

# Reading the JSON file
with open(json_file_path, 'r') as json_file:
    data_read = json.load(json_file)

# Display the content of the JSON file
print("Content of the JSON file:")
for friend in data_read['Friends']:
    name = friend['Name']
    age = friend['Age']
    favorite_color = friend['FavoriteColor']
    print(f"Name: {name}, Age: {age}, Favorite Color: {favorite_color}")
