import os, xml.etree.ElementTree as ET

# Get the directory of the current script
script_folder = os.path.dirname(os.path.abspath(__file__))

# Define the path to your XML file in the same directory as the script
xml_file_path = os.path.join(script_folder, 'sample.xml')

# Create sample XML data
root = ET.Element("Friends")
friend1 = ET.SubElement(root, "Friend")
friend1_name = ET.SubElement(friend1, "Name")
friend1_name.text = "Alice"
friend1_age = ET.SubElement(friend1, "Age")
friend1_age.text = "25"
friend1_favorite_color = ET.SubElement(friend1, "FavoriteColor")
friend1_favorite_color.text = "Red"

friend2 = ET.SubElement(root, "Friend")
friend2_name = ET.SubElement(friend2, "Name")
friend2_name.text = "Bob"
friend2_age = ET.SubElement(friend2, "Age")
friend2_age.text = "30"
friend2_favorite_color = ET.SubElement(friend2, "FavoriteColor")
friend2_favorite_color.text = "Blue"

# Writing the XML data to a file
tree = ET.ElementTree(root)
tree.write(xml_file_path)
print(f"XML file written to {xml_file_path}")

# Reading the XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Display the content of the XML file
print("Content of the XML file:")
for friend in root.findall('Friend'):
    name = friend.find('Name').text
    age = friend.find('Age').text
    favorite_color = friend.find('FavoriteColor').text
    print(f"Name: {name}, Age: {age}, Favorite Color: {favorite_color}")
