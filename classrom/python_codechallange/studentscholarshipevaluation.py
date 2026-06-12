# program for student scholarship evaluation
marks = {
    "Anuj": 92,
    "Rahul": 76,
    "Priya": 88,
    "Neha": 64,
    "Amit": 58,
    "Sneha": 95,
    "Karan": 81,
    "Pooja": 73,
    "Rohit": 47,
    "Anjali": 90
}

#display marks above 85
print("Students Scoring Above 85:")
for student, mark in marks.items():
    if mark > 85:
        print(student)

#topprs
topper = max(marks, key=marks.get)
print("\nTopper:", topper, "(", marks[topper], ")", sep="")

# students with lowest marks
lowest = min(marks, key=marks.get)
print("Lowest Scorer:", lowest, "(", marks[lowest], ")", sep="")

#class average marks 
average = sum(marks.values()) / len(marks)
print("Average Marks:", round(average, 1))

#grade generate 
print("\nGrades:")
for student, mark in marks.items():
    if mark >= 90:
        grade = "A"
    elif mark >= 75:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    else:
        grade = "F"

    print(student, ":", grade)

#list of scholarship of students 

scholarship = []

for student, mark in marks.items():
    if mark >= 90:
        scholarship.append(student)

print("\nScholarship Students:", scholarship)