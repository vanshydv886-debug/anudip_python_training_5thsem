#program for employe salary
file = open("employees.txt", "r")

lines = file.readlines()

high_salary_employees = []

highest_name = ""
highest_salary = 0

lowest_name = ""
lowest_salary = float('inf')

total_salary = 0

high = []
medium = []
low = []

for line in lines:
    emp_id, name, salary = line.strip().split(",")
    salary = int(salary)

    total_salary += salary

    if salary > 50000:
        high_salary_employees.append(name)

    if salary > highest_salary:
        highest_salary = salary
        highest_name = name

    if salary < lowest_salary:
        lowest_salary = salary
        lowest_name = name

    if salary >= 60000:
        high.append(name)
    elif salary >= 40000:
        medium.append(name)
    else:
        low.append(name)

average_salary = total_salary / len(lines)

file.close()

print("Employees Earning Above ₹50,000:")
for employee in high_salary_employees:
    print(employee)

print("\nHighest Paid Employee:", highest_name, f"(₹{highest_salary})")
print("Lowest Paid Employee:", lowest_name, f"(₹{lowest_salary})")
print("Average Salary: ₹", average_salary)

print("\nHigh Salary:", high)
print("Medium Salary:", medium)
print("Low Salary:", low)