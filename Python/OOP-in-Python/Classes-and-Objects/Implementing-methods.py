class Employee:
    # defining the initializer
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department
    
    def tax(self):
        return (self.salary * 0.2)
    
    def salaryPerDay(self):
        return (self.salary / 30)

# Initializing the object for the Employee class
Kinsley = Employee(388700, 5000, "AI & Data")

print("Kinsley's tax is", Kinsley.tax())
print("Monthly salary", Kinsley.salary)
print("Salary per day", Kinsley.salaryPerDay())
print("Department", Kinsley.department)