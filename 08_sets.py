# In set the elements are not repeated
# sets are unordered  
# sets are unindexed  

s = {1,5,7,9,7,7,7,"Rishav"}

s1 = {1 , 4 ,6 ,8, 9,7}
s2 = {5,12,18,7,3}

e = set() # This will create an empty set 

print(type(e))
print(s)

# built in functions

s.add(36) # adds the element in the set
print(s, type(s))

len(s) # give the length of the set
print(s)

s.remove("Rishav") # removes an element
print(s)

s.pop() # removes any random element from the set 
print(s)

print(s1.union(s2)) # gives the union of both the sets  


print(s1.intersection(s2)) # gives the intersection of both the sets


s.clear() #empty the set
print(s)