# Recursion is that when we call the same function 

# factorial using recursion 

def fact(n):
    # base case 
    if(n == 1 or n == 0):
        return 1
    # recursive call 
    return n * fact(n - 1)

n = int(input("Enter a number: "))
print("The factorial is : ",fact(n))