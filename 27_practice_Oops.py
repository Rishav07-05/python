# Q1. 2D vector with 3D vector 

# class TwoDVector:
#     def __init__(self , i , j):
#         self.i = i 
#         self.j = j 
    
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j ")

# class ThreeDVector(TwoDVector):
#     def __init__(self , i , j , k):
#         super().__init__(i,j)
#         self.k = k 

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}k ")


# a =  TwoDVector(1 , 2)
# a.show()
# b = ThreeDVector(1 , 2 , 3)
# b.show()


# Q2. Add bark to dog 

# class Animals:
#     pass
# class Pets(Animals):
#     pass
# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("Bow,Bow !!!")

# doggie = Dog()
# doggie.bark()


# Q3. Add a employee class and add salary and increament properties to it 

class Employee():
    salary = 2345
    increament = 30
    @property # this decorator gives us freedom to return anything we want 
    def salaryAfterIncreament(self):
        return(self.salary + self.salary * (self.increament/100))

e = Employee()
print(e.salary ,e.increament)
print(e.salaryAfterIncreament)