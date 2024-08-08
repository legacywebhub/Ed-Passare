# FOR LOOPS

# For loops are used to repetitively execute a group of statements (or block of code)

'''
for variable in sequence:
    statement(s)
'''

pets = ['cats', 'dogs', 'rabbits']
text = 'Hello World!'


for pet in pets:
    print(pet)

for letter in text:
    print(letter)

for x in range(10):
    print(x)


animal = ['tiger', 'lion', 'dog']
sound = ['roars', 'meows', 'barks']


for x in animal:
    for y in sound:
        print("the "+ x + " "+y)


for x in range(3):
    print("Hello World!")
else:
    print("Loop has ended")


# WHILE LOOPS

# While loops executes a group of statements as long as the given expression is True

i = 0

while i < 5:
    print(i)
    i += 1


i = 1

while i <= 5:
    print("Hello World")
    i = i + 1


x = 100

while x >= 1:
    print(x)
    x = x - 1
else:
    print("Loop has ended")
