#student performance analytic system
# Student Performance Analytics System

# Dictionary containing student records
students = {
    "S101": {"name": "Anuj", "marks": 85},
    "S102": {"name": "Rahul", "marks": 72},
    "S103": {"name": "Aman", "marks": 95},
    "S104": {"name": "Riya", "marks": 45},
    "S105": {"name": "Neha", "marks": 90}
}

while True:

    # Display menu
    print("\n===== STUDENT PERFORMANCE ANALYTICS =====")
    print("1. Display all student records")
    print("2. Search student by ID")
    print("3. Add new student")
    print("4. Update student marks")
    print("5. Delete student")
    print("6. Find topper and lowest scorer")
    print("7. Calculate class average")
    print("8. Count pass and fail students")
    print("9. Generate grades")
    print("10. Display students above average")
    print("11. Display top 5 performers")
    print("12. Scholarship students")
    print("13. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Display all student records
    if choice == 1:

        print("\nStudent Records:")
        for sid, data in students.items():
            print(sid, data)

    # 2. Search student using Student ID
    elif choice == 2:

        sid = input("Enter Student ID: ")

        if sid in students:
            print(students[sid])
        else:
            print("Student Not Found")

    # 3. Add a new student
    elif choice == 3:

        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        marks = int(input("Enter Marks: "))

        students[sid] = {
            "name": name,
            "marks": marks
        }

        print("Student Added Successfully")

    # 4. Update marks of an existing student
    elif choice == 4:

        sid = input("Enter Student ID: ")

        if sid in students:

            marks = int(input("Enter New Marks: "))
            students[sid]["marks"] = marks

            print("Marks Updated Successfully")

        else:
            print("Student Not Found")

    # 5. Delete a student
    elif choice == 5:

        sid = input("Enter Student ID: ")

        if sid in students:

            del students[sid]

            print("Student Deleted Successfully")

        else:
            print("Student Not Found")

    # 6. Find topper and lowest scorer
    elif choice == 6:

        topper = ""
        highest_marks = -1

        lowest_student = ""
        lowest_marks = 101

        for sid, data in students.items():

            if data["marks"] > highest_marks:

                highest_marks = data["marks"]
                topper = sid

            if data["marks"] < lowest_marks:

                lowest_marks = data["marks"]
                lowest_student = sid

        print("\nTopper:")
        print(topper, students[topper])

        print("\nLowest Scorer:")
        print(lowest_student, students[lowest_student])

    # 7. Calculate class average
    elif choice == 7:

        total_marks = 0

        for data in students.values():

            total_marks += data["marks"]

        average = total_marks / len(students)

        print("Class Average =", average)

    # 8. Count pass and fail students
    elif choice == 8:

        pass_count = 0
        fail_count = 0

        for data in students.values():

            if data["marks"] >= 50:
                pass_count += 1
            else:
                fail_count += 1

        print("Pass Students =", pass_count)
        print("Fail Students =", fail_count)

    # 9. Generate grades
    elif choice == 9:

        print("\nStudent Grades:")

        for sid, data in students.items():

            marks = data["marks"]

            if marks >= 90:
                grade = "A"

            elif marks >= 75:
                grade = "B"

            elif marks >= 50:
                grade = "C"

            else:
                grade = "F"

            print(sid, data["name"], "Grade =", grade)

    # 10. Display students scoring above average
    elif choice == 10:

        total_marks = 0

        for data in students.values():

            total_marks += data["marks"]

        average = total_marks / len(students)

        print("Average Marks =", average)

        print("\nStudents Above Average:")

        for sid, data in students.items():

            if data["marks"] > average:

                print(sid, data)

    # 11. Display top 5 performers
    elif choice == 11:

        top_students = sorted(
            students.items(),
            key=lambda x: x[1]["marks"],
            reverse=True
        )

        print("\nTop 5 Performers:")

        for sid, data in top_students[:5]:
            print(sid, data)

    # 12. Create scholarship students dictionary
    elif choice == 12:

        scholarship = {}

        for sid, data in students.items():

            if data["marks"] > 85:

                scholarship[sid] = data

        print("\nScholarship Students:")
        print(scholarship)

    # 13. Exit
    elif choice == 13:

        print("Program Ended Successfully")
        break

    else:
        print("Invalid Choice")