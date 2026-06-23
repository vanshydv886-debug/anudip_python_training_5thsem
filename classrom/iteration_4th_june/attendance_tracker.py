#program for attendance counter
student = 1
present = 0
absent = 0

while student <= 30:
    status = input(f"Student {student} attendance (Present/Absent): ")

    if status == "Present":
        present += 1
    elif status == "Absent":
        absent += 1
    else:
        print("Invalid input")

    student += 1

print("No of Students Present:", present)
print("No of Students Absent:", absent)