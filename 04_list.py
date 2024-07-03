# Lists are mutable 
# Lists are a container to store a element of same datatype

store = ["Apple","Mango",False,5,4.3,"Rishav"]
l1 = [1.4,9,23,8,12,44]
print(store[2])
store[0] = "Hero" #list can be change as they are mutable 
print(store[0])


# indexing in list 
print(store[0:3])


# Inbuilt functions in List
store.append("Added") #add the element at the end of the index
print(store)

l1.sort() # Sorts the list
print(l1)

l1.reverse() #Reverses the list
print(l1)

l1.insert(3,"Hola") #inserts the value at desired index
print(l1)

print(l1.pop(3)) #show the element to remove 
print(l1) # remove the value at given index and the rest element are returned 

l1.remove(44) # remove the given element
print(l1)
