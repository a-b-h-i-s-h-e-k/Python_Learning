'''

# Loop Through a Tuple
--> we can loop through the tuple items by using a 'for' loop.
--> Iterate through the items and print the values

# Loop Through the Index Numbers
--> You can also loop through the tuple items by referring to their index number.
--> Use the range() and len() functions to create a suitable iterable.

'''

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
    

thistuple1 = ("apple", "banana", "cherry")
for i in range(len(thistuple1)):
    print(thistuple1[i])
    
    
'''
# Using a While Loop
--> You can loop through the tuple items by using a while loop.
--> Use the len() function to determine the length of the tuple, then start 
at 0 and loop your way through the tuple items by referring to their indexes.
--> Remember to increase the index by 1 after each iteration.

'''

thistuple2 = ("apple", "banana", "cherry")
i = 0 
while i < len(thistuple2):
    print(thistuple2[i])
    i = i + 1
