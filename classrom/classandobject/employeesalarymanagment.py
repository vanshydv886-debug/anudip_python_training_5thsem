#profram for  Employee Salary Management 

#creating employee class :
class employee :

    #constructor to initialize object '
    def __init__(self, emp_id, name, salary):
        self.emp_id = ""
        self.name = ""
        self.salary = 0

    #display details of employee
    def display_details(self):
        print("\n----- Employee Details -----")
        print("Employee ID     :", self.emp_id)
        print("Employee Name   :", self.name)
        print("Monthly Salary  : ₹", self.salary)

    #method to calculate annual salary
    def annual_salary(self):
        annual = self.salary * 12       #without make method object cannot be call
        print("annual income : ", annual)

    #method to increase salary by a given method
    def increase_salary(self):
        increase = self.salary * percentage / 100
        self.salary += increase
        print("Updated Salary  : ₹", self.salary)

#take input from the user

emp_id = input("Enter Employee ID : ")
name = input("Enter Employee Name : ")

#salary validation 
while true:
    try:
        salary = int(input("enter the salary : "))
        if salary > 0:
            break
        else :
            print("salary must be gretaer than 0 :")
    except ValueError:
        print("Invalid Input! Enter numeric value.")

# Creating object
emp = Employee(emp_id, name, salary)

# Display details
emp.display_details()

# Calculate annual salary
emp.annual_salary()

# Increase salary
while True:
    try:
        percentage = float(input("Enter Percentage Increase: "))
        if percentage >= 0:
            break
        else:
            print("Percentage cannot be negative.")
    except ValueError:
        print("Invalid Input! Enter numeric value.")

emp.increase_salary(percentage)





