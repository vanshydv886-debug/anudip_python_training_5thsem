# Student Result Management System
# This program takes marks of 5 subjects and calculates total, percentage, grade and failed subjects

# Input marks of 5 subjects
m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))

# Calculate total marks
total = m1 + m2 + m3 + m4 + m5

# Calculate percentage (assuming each subject is out of 100)
percentage = (total / 500) * 100

# Count failed subjects
failed = 0

if m1 < 40:
    failed += 1
if m2 < 40:
    failed += 1
if m3 < 40:
    failed += 1
if m4 < 40:
    failed += 1
if m5 < 40:
    failed += 1

# Grade calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

# Output results
print("\n----- RESULT -----")
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Subjects Failed:", failed)