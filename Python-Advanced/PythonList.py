# four collection data types in Python:

# List is a collection which is ordered and changeable. Allows duplicate members. written with square brackets.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members. written with round brackets.
# Set is a collection which is unordered and unindexed. No duplicate members. written with curly brackets.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members. They have keys and values. written with curly brackets.

#################################  List ##############################################################

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # print 1st item in list
for x in thislist: # loop over list
  print(x)
if "apple" in thislist: # Check if Item Exists
  print("Yes, 'apple' is in the fruits list")
print("apple" in thislist)
print(len(thislist)) # List Length
thislist.append("orange") # Add Items
mylist = thislist.copy() # create copy of list
thislist.reverse() # reverse the list in-place
thislist.sort() # sort the list in ascending order
thislist.sort(reverse=True) # sort the list in descending order

# sort based on logic defined in a function
# In sort, when the key is given as a function, then the value returned by the function( for each item in list) is used to sort the items.
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc) # sorts the items in ascending order of their lengths

# Sort a list of dictionaries based on the "year" value of the dictionaries:
def myFunc2(e):
  return e['year']
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc2)


