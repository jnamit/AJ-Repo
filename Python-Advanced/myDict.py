thisdict ={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
val_list = thisdict.values()
print ("val_list = ", val_list)
for x in val_list:
    print (x)
for x in thisdict:
    print (thisdict[x])

print ( list(thisdict.keys())[0] )     # key of "first" element
print ( list(thisdict.values())[0] )  # value of "first" element
print ( list(thisdict.items())[0] )   # (key, value) tuple of "first" element