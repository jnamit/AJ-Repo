# Set is a collection which is unordered and unindexed. No duplicate members. written with curly brackets.

############### SET #############
thisset = {"apple", "banana", "cherry"}
for x in thisset: # loop over a set
    print(x) #Sets are unordered, so the items may print in a random order
print("banana" in thisset) # contains

#Once a set is created, you cannot change its items, but you can add new items.
thisset.add("orange") # add an item
print(thisset)
thisset.add("banana") # add item that already exists, set will not change
print(thisset)
thisset.update(["orange", "mango", "grapes"]) # add a list of items to set using UPDATE method
print(thisset)
print(len(thisset)) # length
thisset.remove("banana")  #If the item to remove does not exist, remove() will raise an error.
print(thisset)
thisset.discard("banana") #If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop(), method to remove an item, but this method will remove the last item.
# Remember that sets are unordered, so you will not know what item that gets removed.
# The return value of the pop() method is the removed item.
x = thisset.pop()
print(x)
print("thisset = ", thisset)
thatset = thisset.copy()
print("thatset = ", thatset)

# Other set operations like difference, union, intersection, isdisjoint(),
# issubset(), issuperset(), symmetric_difference()

# symmetric_difference: Returns a set that contains all items from both sets,
# except items that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print("symmetric_difference = ",z) # apple will not be printed

