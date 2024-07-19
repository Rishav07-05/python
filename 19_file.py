# Files I/O mainly helps in reading and writing the other files or we can say that it helps to extract data 

# We are going to read the data inside the txt file with the help of some build in functions in python



# To read a file 

# f = open("file.txt")
# data = f.read()
# print(data)
# f.close() # Whenever we open a file it's a mandatory to close it 

# To write a file

# st = "Hey Rishav how are you"
# f = open("myfile.txt", "w")
# f.write(st)
# f.close()


# More file functions
 
# Readlines function 

# f = open("file.txt")
# lines = f.readlines()
# print(lines , type(lines))
# f.close()

# Readline function

# f = open("file.txt")
# lines = f.readline()

# while(lines != ""):
#     print(lines)
#     lines = f.readline()

# f.close()


# for appending in the last of a file we use append function 

# st = "Batman"
# f = open("file.txt" , "a") # here the last a represent the appending of the data inserted in the st 
# f.write(st)
# f.close()


# With statement ==> automatically closes the file 

with open("file.txt") as f:
    print(f.read())

# we need not to explicitly close the file 