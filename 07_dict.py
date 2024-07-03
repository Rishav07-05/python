# Dictionary are the key value pairs
# Dictionaries are mutable
# Ordered doesn't matter 
# Properly Indexed and can't be duplicated

marks = {
    "Rishav" : 100,
    "Ram" : 90,
    "Sita" : 80
} 

# print(marks , type(marks))
# print(marks["Rishav"])

# Built in function in dictionary

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Rishav": 99 , "Hoii": 100})
print(marks)

print(marks.get("Holi"))