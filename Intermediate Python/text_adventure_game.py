import re

def handle_command(command):
    if re.match(r"^go north$", command):
        return "You move north."
    elif re.match(r"^pick up apple$", command):
        return "You picked up an apple."
    else:
        return "I don't understand that command."

# Game loop
while True:
    command = input("Enter a command: ")
    result = handle_command(command)
    print(result)
    if command == "quit":
        break
