class Employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

    # Method to update the salary
    def update_salary(self, new_salary):
        self.salary = new_salary

    # Method to display employee details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")

    # Method to calculate annual income
    def calculate_annual_income(self):
        return self.salary * 12

# Create instances for three employees
employee1 = Employee("John Doe", "Software Engineer", 5000)
employee2 = Employee("Jane Smith", "Manager", 7000)
employee3 = Employee("Robert Brown", "HR Specialist", 4000)

# Display details for each employee
print("Employee 1 Details:")
employee1.display_details()
print(f"Annual Income: {employee1.calculate_annual_income()}\n")

print("Employee 2 Details:")
employee2.display_details()
print(f"Annual Income: {employee2.calculate_annual_income()}\n")

print("Employee 3 Details:")
employee3.display_details()
print(f"Annual Income: {employee3.calculate_annual_income()}\n")

# Update salary of employee1 and display the updated details
employee1.update_salary(6000)
print("Updated Employee 1 Details:")
employee1.display_details()
print(f"Updated Annual Income: {employee1.calculate_annual_income()}")
