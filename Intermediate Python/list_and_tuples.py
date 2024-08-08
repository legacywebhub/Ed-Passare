# LISTS

'''A list is a collection where you can keep many items together'''

# Creating a list of marvel characters
my_items = ['spiderman', 'hulk', 'panther', 'dr. strange', True, 1.23, [1, 2, 3]]

#print(my_items)

'''You can do lots of things with lists, like adding new items or taking some out.'''
#print(my_items)

# Adding a new character to the list
#my_items.append('loki')

#print(my_items)

# Removing a character from the list
#my_items.remove('hulk')

# Printing all characters in the list
#print(my_items)

# Fetching an item at an index
my_best_character = my_items[0]

#print(my_best_character)

# Fetching my favourite characters
my_best_best_characters = my_items[0:3]

#print(my_best_best_characters)


#print(len(my_items))


dave_favourite_marvel_characters = my_items.copy()

#print(dave_favourite_marvel_characters)





# TUPLES

'''A tuple is simply a list but doesn't change'''

# Creating a tuple for a pair of socks
socks = ('blue', 'red', 'green', "pink")

# Accessing items in a tuple
# first_sock = socks[0]
# second_sock = socks[1]

# Printing the socks
print("First sock:", socks[0])