# Q1. Table using loop
# a = int(input("Enter your number: "))
# for i in range(1,11,1):
#     mul = a * i
#     print(a,"*",i,"=" ,mul)

# Q2. To greet all person in a list whose name starts with R 
# list = ["Rohan" , "Ram" , "Sohan" , "Rishav" , "Tony"]
# for item in list:
#     store = item
#     for item in item:
#         if(item == "R"):
#             print("Good Moring:",store)

# Q3. Find a number is prime or not 
# a = int(input("Enter your number: "))
# count = 0
# for i in range(2,a):
#     if(a%i == 0):
#         count+=1
# if(count < 2):
#     print("Prime Number")
# else:
#     print("Not Prime")
    

# Q4. Sum of first n natural numbers 
# a = int(input("Enter your number: "))
# sum = 0
# for i in range(0,a+1,1):
#     sum+=i
# print(sum)


# Q5. Calculate the factorial 
# a = int(input("Enter your number: "))
# fact = 1
# for i in range(1,a+1,1):
#     fact = fact * i
# print(fact)


# Q6. Print table in reverse order 
# a = int(input("Enter your number: "))
# for i in range(10,0,-1):
#     print(a, "*", i, "=", a*i)


# Q7. Star Pattern
'''
  *
 ***
*****
'''
# a = int(input("Enter your number: "))
# for i in range(1, a+1):
#     print(" "* (2*i-1), end="")
#     print("*"* i, end="")
#     print("\n")

# Q8 . Star Pattern 
'''
* * *
*   *
* * *
'''

a = int(input("Enter your number: "))
for i in range(1, a+1):
    if(i == 1 or i == a):
        print("*" * a, end="")
    else:
        print("*", end="")
        print(" "* (a - 2), end="")
        print("*", end="")
    print("")