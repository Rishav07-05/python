# Q1. Find greatest of three 

# def greatest(a,b,c):
#     if(a > b and a > c):
#         print("I am the greatest",a)
#     elif(b > a and b > c):
#         print("I am the greatest",b)
#     else:
#         print("I am the greatest",c)
    
# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
# greatest(a,b,c)


# Q2. Convert farenheit into celcius 

# def temp(a):
#     celsius = (a - 32)/1.8
#     print(celsius)

# a = int(input("Enter your temperature: "))
# temp(a)


# Q3. Sum of first n natural numbers using recursion

# def sum(a):
#     if(a == 1):
#         return 1
    
#     return sum(a - 1) + a

# a = int(input("Enter your number: "))
# z = sum(a)
# print(z)


# Q4. star pattern 

# def star(n):
#     for i in range(n,0,-1):
#         print("*" * i , end="")
#         print("\n")

# n = int(input("Enter your number: "))
# star(n)

# Q5. Remove a given word from list 

# def remove(a):
#     for item in list:
#         if(a == item):
#             list.remove(a)
#     print(list)

# list = ["hello" , "hh" , "9" , 9]
# a = (input("Enter your number: "))
# remove(a)

# Q6. Print table 

# def table(a):
#     for i in range(1,11,1):
#         print(a,"*",i,"=",a*i)

# a = int(input("Enter your number: "))
# table(a)