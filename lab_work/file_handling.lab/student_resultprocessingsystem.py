#program ysed to
# Function to display all student records
def display_records():

    # Open file in read mode
    f = open("results.txt", "r")

    # Read and display each record
    for line in f:
        print(line.strip())

    # Close file
    f.close()


# Function to search student using Student ID
def search_student():

    sid = input("Enter Student ID: ")

    # Open file
    f = open("results.txt", "r")

    found = False

    # Search record line by line
    for line in f:

        data = line.strip().split(",")

        if data[0] == sid:
            print("ID:", data[0])
            print("Name:", data[1])
            print("Marks:", data[2])

            found = True

    # If record not found
    if found == False:
        print("Student Not Found")

    f.close()


# Function to find topper and lowest scorer
def topper_lowest():

    f = open("results.txt", "r")

    # Initial values
    topper_marks = -1
    lowest_marks = 101

    topper = ""
    lowest = ""

    # Read file
    for line in f:

        data = line.strip().split(",")

        marks = int(data[2])

        # Find topper
        if marks > topper_marks:
            topper_marks = marks
            topper = data[1]

        # Find lowest scorer
        if marks < lowest_marks:
            lowest_marks = marks
            lowest = data[1]

    print("Topper =", topper, topper_marks)
    print("Lowest =", lowest, lowest_marks)

    f.close()


# Function to calculate class average
def class_average():

    f = open("results.txt", "r")

    total = 0
    count = 0

    # Calculate total marks and student count
    for line in f:

        data = line.strip().split(",")

        total += int(data[2])
        count += 1

    print("Average =", total / count)

    f.close()


# Function to count pass and fail students
def pass_fail():

    f = open("results.txt", "r")

    passed = 0
    failed = 0

    for line in f:

        data = line.strip().split(",")

        # Passing marks = 40
        if int(data[2]) >= 40:
            passed += 1
        else:
            failed += 1

    print("Pass =", passed)
    print("Fail =", failed)

    f.close()


# Function to generate grades
def generate_grades():

    f = open("results.txt", "r")

    for line in f:

        data = line.strip().split(",")

        marks = int(data[2])

        # Grade Calculation
        if marks >= 90:
            grade = "A"

        elif marks >= 75:
            grade = "B"

        elif marks >= 40:
            grade = "C"

        else:
            grade = "F"

        print(data[1], "-", grade)

    f.close()


# Function to create grades.txt file
def create_grade_file():

    # Open source file
    f = open("results.txt", "r")

    # Open destination file
    g = open("grades.txt", "w")

    for line in f:

        data = line.strip().split(",")

        marks = int(data[2])

        # Grade Calculation
        if marks >= 90:
            grade = "A"

        elif marks >= 75:
            grade = "B"

        elif marks >= 40:
            grade = "C"

        else:
            grade = "F"

        # Write grade report into new file
        g.write(data[0] + "," + data[1] + "," + grade + "\n")

    f.close()
    g.close()

    print("grades.txt created successfully")


# Main Menu
while True:

    print("\n1. Display Records")
    print("2. Search Student")
    print("3. Topper and Lowest")
    print("4. Class Average")
    print("5. Pass and Fail")
    print("6. Generate Grades")
    print("7. Create grades.txt")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    # Call display function
    if choice == 1:
        display_records()

    # Call search function
    elif choice == 2:
        search_student()

    # Call topper function
    elif choice == 3:
        topper_lowest()

    # Call average function
    elif choice == 4:
        class_average()

    # Call pass/fail function
    elif choice == 5:
        pass_fail()

    # Call grade generation function
    elif choice == 6:
        generate_grades()

    # Create grades.txt file
    elif choice == 7:
        create_grade_file()

    # Exit program
    elif choice == 8:
        print("Program Ended")
        break

    # Invalid menu choice
    else:
        print("Invalid Choice")