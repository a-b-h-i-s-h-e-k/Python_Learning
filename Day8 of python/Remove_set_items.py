'''
# Remove Item:->
-> To remove an item in a set, use the remove(), or the discard() method.
-> Note: If the item to remove does not exist, remove() will raise an error.

-> Remove "banana" by using the discard() method.
-> Note: If the item to remove does not exist, discard() will NOT raise an error.

'''

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


thisset1 = {"apple", "banana", "cherry"}
thisset1.discard("banana")
print(thisset1)

'''
--> You can also use the pop() method to remove an item, 
but this method will remove a random item, so you cannot 
be sure what item that gets removed.

--> The return value of the pop() method is the removed item.

--> Remove a random item by using the pop() method.

--> Note: Sets are unordered, so when using the pop() method, 
you do not know which item that gets removed.
''' 

thisset2 = {"apple", "banana", "cherry"}
x = thisset2.pop()
print(x)
print(thisset2) 

# The clear() method empties the set

thisset3 = {"apple", "banana", "cherry"}
thisset3.clear()
print(thisset3) 

# The del keyword will delete the set completely.

thisset4 = {"apple", "banana", "cherry"}
del thisset4
print(thisset4)
