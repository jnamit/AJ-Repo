# Dictionary is a collection which is unordered, changeable and indexed.
# No duplicate members.
# They have keys and values. written with curly brackets.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

x = thisdict["model"] # access the items of a dictionary by referring to its key name, inside square brackets
print("x = ", x)
thisdict["year"] = 2018
print(thisdict)
for x in thisdict: # loop over keys
  print("looping over keys" , x)
for y in thisdict.values(): # loop over values
  print("looping over values" , y)
for x, y in thisdict.items(): # loop over key and value at the same time
  print(x, y)
if "model" in thisdict: # check if a key exists
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
print(len(thisdict))
thisdict["color"] = "red" # add a new item
print(thisdict)
thisdict.pop("model") # removes the item with the specified key name
print(thisdict)

# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a
# reference to dict1, and changes made in dict1 will automatically also be made in dict2.
mydict = thisdict.copy()
print("mydict = ", mydict)