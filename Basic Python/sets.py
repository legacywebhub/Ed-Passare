'''
A set is simply a list but ignores duplicates
'''

nums = {0, 0, 0, 1, 1, 2, 3}

# Create an iterator for the set
iterator = iter(nums)

# Get the first item (to skip it)
next(iterator)

# Get the second item
second_item = next(iterator)

# Get the third item
third_item = next(iterator)


print(second_item)
print(third_item)

set = {"a", "b", "c", "d", "a", "b"}
converted_set = list(set)

print(set)
print(converted_set)
print(converted_set[0])