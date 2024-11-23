'''
# Add Items
-> Once a set is created, you cannot change its items, but you can add new items.
-> To add one item to a set use the add() method.

'''

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# ADD SETS:--> To add items from another set into the current set, use the update() method.

thisset1 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset1.update(tropical)
print(thisset1)

# Add Any Iterable:->
# -> The object in the update() method does not have to be a set, 
# it can be any iterable object (tuples, lists, dictionaries etc.).

thisset2 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset2.update(mylist)
print(thisset2)

thisset3 = {"apple", "banana", "cherry"}
mytuple = ("kiwi", "orange")
thisset3.update(mytuple)
print(thisset3)
