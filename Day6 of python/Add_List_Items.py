# Append Items:-> To add an item to the end of the list, use the append() method

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items:-> To insert a list item at a specified index, use the insert() method. and it insert at specified index.

thislist.insert(1, "kiwi")
print(thislist)

# Extend List:-> To append elements from another list to the current list, use the extend() method.

thislist = ['apple', 'kiwi', 'banana', 'cherry', 'orange']
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)



# Add Any Iterable
# -> The extend() method does not have to append lists, you can add any 
# iterable object (tuples, sets, dictionaries etc.).

thistuple = ('kiwi','orange')
thislist.extend(thistuple)
print(thislist)