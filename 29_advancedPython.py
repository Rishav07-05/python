# Walrus Operators ":="

# if(n := len([1, 2, 3, 4, 5])) > 3:
#     print(f"List is too long ({n} elements, expected <= 3)")


# Type Operator 

# n : int = 5

# name : str = "Rishav"

# def sum(a: int, b: int) -> int:
#     return a+b


# Exception Handling 

# try:
#     a = int(input("Hey, Enter a number: "))
#     print(a)
# except Exception as e:
#     print(e)



# Map 

# l = [1 ,2 , 3, 4 , 5]
# square = lambda y: y*y

# sqlist = map(square, l)
# print(list(sqlist))

# Filter

# l = [1 ,2 , 3, 4 , 5]
# def even(n):
#     if(n%2 == 0):
#         return True
#     return False

# onlyEven = filter(even , l)
# print(list(onlyEven))

# Reduce


# from functools import reduce

# l = [1 ,2 , 3, 4 , 5]

# def sum(a,b):
#     return a + b
# print(reduce(sum , 1))