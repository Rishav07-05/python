# Tuples also acts as a container 
# But are totally immutable


a = (1,20,29,45,45,2,"Rishav")
b = (1,23,45,"Hello")
print(type(a))


# Inbuilt functions in tuple

cnt = a.count(45) # counts the element
print(cnt)

idx = a.index(45) # give the first occurence index of element inserted
print(idx)

concatenated = a + b #add up two tuples
print(concatenated)

repeat = b * 4 #repeat the tuple for the desired time 
print(repeat)

print(len(a)) # gives the length of tuple