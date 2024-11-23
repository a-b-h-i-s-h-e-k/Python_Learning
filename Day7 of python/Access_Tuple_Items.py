# We can access tuple items by referring to the index number, inside square brackets.

'''
# Negative Indexing
--> Negative indexing means start from the end.
--> -1 refers to the last item, -2 refers to the second last item etc.

# Range of Indexes
--> we can specify a range of indexes by specifying where to start and where to end the range.
--> When specifying a range, the return value will be a new tuple with the specified items.

--> Note: The search will start at index 2 (included) and end at index 5 (not included).

'''


thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print(thistuple[-1])

print(thistuple[2:5])

# By leaving out the start value, the range will start at the first item.
thistuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple1[:4])

# By leaving out the end value, the range will go on to the end of the tuple.
print(thistuple1[2:])

# Range of Negative Indexes
# --> Specify negative indexes if you want to start the search from the end of the tupleThis example returns the items from index -4 (included) to index -1 (excluded)
# --> This example returns the items from index -4 (included) to index -1 (excluded).

thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple2[-4:-1])

# Check if item Exists
# --> To determine if a specified item is present in a tuple use the in keyword

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") 




