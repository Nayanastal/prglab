class Employee:
    company_name="ABCD"
    location="calicut"
    def __init__(self,id,name,salary):
        self.emp_id=id
        self.emp_name=name
        self.emp_salary=salary
    def details(self):
        print(self.emp_id,self.emp_name,self.emp_salary)
emp1=Employee(101,"Manu",50000)
emp2=Employee(102,"Hari",25000)
print("company name:",Employee.company_name,"Location:",Employee.location)
emp1.details()
emp2.details()
