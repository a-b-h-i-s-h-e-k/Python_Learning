'''
# Slicing

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

Note: The first character has index 0.

'''

b = "Hello World"
print(b[2:5])

'''
Slice From the Start
-> By leaving out the start index, the range will start at first character.

-> Get the characters from the start to position 5 (not included):
'''

print(b[:5])

'''
Slice To the End

-> By leaving out the end index, the range will go to the end:

-> Get the characters from position 2, and all the way to the end
'''

print(b[2:])

'''
Negative Indexing:
we use negative indexes to start the slice from the ned of the string;

Example:

Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
'''
print(b[-5: -2])



