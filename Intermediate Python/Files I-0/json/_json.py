## What is JSON

'''
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write 
and easy for machines to parse and generate. It is commonly used for transmitting data in web applications.

Imagine you have a notebook where you write information in a very organized way using pairs. 
Each piece of information has a key (like a name) and a value (like the person's age). 
For example, if you write about your friends, you might have a key for each friend's name and a value for their age. 
This special notebook is like a JSON file.
'''

## Python code:

import os, json

# Get the directory of the current script
script_folder = os.path.dirname(os.path.abspath(__file__))

# Define the path to your JSON file in the same directory as the script
json_file_path = os.path.join(script_folder, 'sample.json')

# Create sample JSON data
data = {
    "FavoriteHeroes": [
        {
            "Name": "Spiderman",
            "Universe": "Marvel",
            "SuperPowers": ['Strength', 'Flight'],
        },
        {
            "Name": "Superman",
            "Universe": "DC",
            "SuperPowers": ['Super Strength', 'Flight', 'Laser Eyes', 'Super Healing', 'Speed']
        },
        {
            "Name": "Green Latern",
            "Universe": "DC",
            "SuperPowers": ['Flight', 'Strength', 'Magic Ring']
        }
    ]
}

# Writing the data to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file)
print(f"JSON file written to {json_file_path}")

# Reading the JSON file
with open(json_file_path, 'r') as json_file:
    data_read = json.load(json_file)

# Display the content of the JSON file
print("Content of the JSON file:")
for hero in data_read['FavoriteHeroes']:
    name = hero['Name']
    universe = hero['Universe']
    super_powers = hero['SuperPowers']
    print(f"Name: {name}, Universe: {universe}, Super Powers: {super_powers}")
