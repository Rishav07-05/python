class Employee:
    language = "Go" 
    salary = 19000000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def __init__(self,name,language,salary): # dunder method which is automatically called
        self.name = name
        self.language = language
        self.salary = salary 

    def greet(self):
        print("Good Night")

    # if we don't want to put the self method as it's bulky then we can use :
    @staticmethod
    def greetAgain():
        print("Good Night Again")



rishav = Employee("Rishav" , "Javascript" , 1000000)
# rishav.language = "HTML" 

print(rishav.name ,  rishav.salary , rishav.language)