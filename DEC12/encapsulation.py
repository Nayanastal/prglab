class Employee:
    def __init__(self,name,salary):
        #public member
        self.name=name
        #private member not accessible outside the class
        self.__salary=salary
    def show(self):
        print("Name is ",self.name,"and salary is ",self.__salary)
emp=Employee("jessa",40000)
emp.show()
print(emp.name)
