# Q1. Storing values of programmers working at microsoft 

# class Programmer:
#     def __init__(self,name,company,salary,language):
#         self.name = name
#         self.company = company
#         self.salary = salary
#         self.language = language

# store = Programmer("Rishav" , "Microsoft" , "1000000" , "Go")
# store1 = Programmer("Ram" , "Microsoft" , "1000000" , "Go")
# store2 = Programmer("Sohan" , "Microsoft" , "1000000" , "Go")
# store3 = Programmer("Rohan" , "Microsoft" , "1000000" , "Go")

# print(store.name ,  store.company, store.salary, store.language)
# print(store1.name ,  store1.company, store1.salary, store1.language)
# print(store2.name ,  store2.company, store2.salary, store2.language)
# print(store3.name ,  store3.company, store3.salary, store3.language)


# Q2. Make calculator capable of finding squares, cubes and square root 


# import math 


# class calculator:
#     def __init__ (self , n , a):
#         if(n == "sqrt"):
#             print(f"The square root of {a} is {math.sqrt(a)}")

#         elif(n == "square"):
#             print(f"The square of {a} is {a ** 2}")

#         elif(n == "cube"):
#             print(f"The square of {a} is {a ** 3}")
#         else:
#             print("Something went wrong...")


# n = input("Enter the operation you want to perform: ")
# a = int(input("Enter the number: "))

# store = calculator(n , a)



# it's not always mandatory to use self we can the name of self to anything like "Rishav" , "hhah" 