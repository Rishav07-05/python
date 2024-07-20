# class Employee:
#     company = "ITC"
#     def show(self):
#         print(f"The name of the employee is {self.name} and the salary is {self.salary}")


# class programmer(Employee):
#     company = "Infotech"
#     def showLang(self):
#         print(f"The name is {self.name} and the language he use most is {self.language}")

# a = Employee()
# b = programmer()

# print(a.company ,b.company)



# Multiple Inheritence 

# class Employee:
#     company = "ITC"
#     def show(self):
#         print(f"The name of the employee is {self.name} and the salary is {self.salary}")


# class coder:
#     language = "py"
#     def printlang(self):
#         print(f"Out of all he chooses: {self.language}")



# class coderName:
#     name = "Rishav"
#     def printName(self):
#         print(f"Name of the coder is: {self.name}")


# class programmer(Employee , coder ,coderName):
#     company = "Infotech"
#     def showLang(self):
#         print(f"The name is {self.name} and the language he use most is {self.language}")

# a = Employee()
# b = programmer()

# print(b.language)   
# b.printlang()
# b.showLang()


# Multi Level Inheritence 


# class employee:
#     a = 1
# class programmer(employee):
#     b = 2
# class manager(programmer):
#     c = "Everything is here ..."

# o = employee()
# print(o.a)
# # print(o.b) # Shows error 
# # print(o.c) # Shows error

# o = programmer()
# print(o.b)
# print(o.a)
# # print(o.c) # Shows error

# o = manager()
# print(o.b)
# print(o.a)
# print(o.c)


# Super Keyword 

# class employee:
#     def __init__(self):
#         print("Constructor of Employee")
#     a = 1
# class programmer(employee):
#     def __init__(self):
#         print("Constructor of programmer")
#     b = 2
# class manager(programmer):
#     def __init__(self):
#         super().__init__() # basically calls the child class
#         print("Constructor of manager")
#     c = "Everything is here ..."

# # o = employee()
# # print(o.a)


# # o = programmer()
# # print(o.b)

# o = manager()
# print(o.c , o.b , o.a)


# Decorators 

# class Employee:
#     a = 1
#     @classmethod # Helps to show the class attribute by overridding the values of instance attributes
#     def show(cls):
#         print(f"the class attribute of a is {cls.a}")

# e = Employee()
# e.a = 45
# e.show()


# Property decorators 

class Employee:
    a = 1
    @classmethod # Helps to show the class attribute by overridding the values of instance attributes
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

    @property
    def name(self):
        return self.ename
    @name.setter
    def name(self,value):
        self.ename = value

e = Employee()
e.a = 45
e.name = "Rishav"
print(e.name)
e.show()