# LISTS

'''A list is a collection where you can keep many items together'''

# Creating a list of marvel characters
my_favorite_marvel_characters = ['spiderman', 'hulk', 'panther', 'dr. strange']

'''You can do lots of things with lists, like adding new toys or taking some out.'''
#print(my_favorite_marvel_characters)

# Adding a new character to the list
#my_favorite_marvel_characters.append('loki')

#print(my_favorite_marvel_characters)

# Removing a character from the list
#my_favorite_marvel_characters.remove('hulk')

# Printing all characters in the list
#print(my_favorite_marvel_characters)

# Fetching an item at an index
my_best_character = my_favorite_marvel_characters[0]

print(my_best_character)

# Fetching my favourite characters
my_best_best_characters = my_favorite_marvel_characters[0:3]

print(my_best_best_characters)


print(len(my_favorite_marvel_characters))


dave_favourite_marvel_characters = my_favorite_marvel_characters.copy()

print(dave_favourite_marvel_characters)





# TUPLES

'''A tuple is simply a list but doesn't change'''

# Creating a tuple for a pair of socks
socks = ('blue', 'red', 'green', "pink")

# Accessing items in a tuple
first_sock = socks[0]
second_sock = socks[1]

# Printing the socks
#print("First sock:", first_sock)
#print("Second sock:", second_sock)