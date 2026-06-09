 # Employee Performance Evaluation with Validation

employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

# Validation
valid_employees = []

for emp in employees:

    if len(emp) != 3:
        print("Invalid Record:", emp)
        continue

    emp_id = emp[0]
    name = emp[1]
    score = emp[2]

    if not isinstance(emp_id, str) or emp_id == "":
        print("Invalid Employee ID:", emp)
        continue

    if not isinstance(name, str) or name == "":
        print("Invalid Employee Name:", emp)
        continue

    if not isinstance(score, (int, float)):
        print("Invalid Score:", emp)
        continue

    if score < 0 or score > 100:
        print("Score Out of Range:", emp)
        continue

    valid_employees.append(emp)

# Task 1
print("Employees Scoring 80 or Above:")
for emp in valid_employees:
    if emp[2] >= 80:
        print(emp[0], emp[1], emp[2])

# Task 2
count = 0

for emp in valid_employees:
    if emp[2] < 60:
        count += 1

print("\nEmployees Needing Improvement:", count)

# Task 3
highest = valid_employees[0]

for emp in valid_employees:
    if emp[2] > highest[2]:
        highest = emp

print("\nHighest Performer:")
print(highest[0], highest[1], highest[2])

# Task 4
high_performers = []

for emp in valid_employees:
    if emp[2] > 75:
        high_performers.append(emp[1])

print("\nHigh Performers:", high_performers)

# Task 5
print("\nPerformance Categories:")

for emp in valid_employees:

    score = emp[2]

    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"

    print(emp[1], "->", category)