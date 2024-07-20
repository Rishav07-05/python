class Employee:
    language = "Go" 
    salary = 19000000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good Night")

    # if we don't want to put the self method as it's bulky then we can use :
    @staticmethod
    def greetAgain():
        print("Good Night Again")



rishav = Employee()
rishav.language = "Js" 


# two ways of asking the values from the function 
rishav.greet()
rishav.greetAgain()
rishav.getInfo()
# Employee.getInfo(rishav)