# Tuple is a collection which is ordered and unchangeable. Allows duplicate members. written with round brackets.


######################################################################################################
#################################  Tuples ############################################################
######################################################################################################
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # indexing begins from 0
for x in thistuple: # this is how you loop over tuples
    print(x)
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
print("apple" in thistuple)
print(len(thistuple))

thattuple = ("apple", "banana", "cherry", "banana")
print("num of bananas:", thattuple.count("banana")) # count number of times an item appears
print("position of cherry:", thattuple.index("cherry")) # position of an item

#thistuple[3] = "orange" # Tuples are unchangeable, can't add/delete items. This will raise an error

