# Student Information System using Class, Object, Methods and Menu

# Creating Student class
class Student:

    # Constructor to initialize variables
    def __init__(self):
        self.roll_no = ""
        self.name = ""
        self.marks = 0

    # Method to input student details
    def get_data(self):

        # Input roll number
        self.roll_no = input("Enter Roll Number: ")

        # Validation for student name
        while True:
            self.name = input("Enter Student Name: ")

            if self.name.replace(" ", "").isalpha():
                break
            else:
                print("Invalid Name! Enter alphabets only.")

        # Validation for marks
        while True:
            try:
                self.marks = float(input("Enter Marks (0-100): "))

                if 0 <= self.marks <= 100:
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Invalid Input! Enter numeric value.")

    # Method to display student details
    def display(self):

        # Check if data exists
        if self.name == "":
            print("No Student Record Found!")
        else:
            print("\n----- Student Details -----")
            print("Roll Number :", self.roll_no)
            print("Name        :", self.name)
            print("Marks       :", self.marks)

    # Method to calculate and display grade
    def grade(self):

        # Check if data exists
        if self.name == "":
            print("No Student Record Found!")
            return

        # Grade calculation
        if self.marks >= 90:
            grade = "A+"
        elif self.marks >= 80:
            grade = "A"
        elif self.marks >= 70:
            grade = "B"
        elif self.marks >= 60:
            grade = "C"
        elif self.marks >= 50:
            grade = "D"
        else:
            grade = "F"

        print("Grade :", grade)


# Creating object of Student class
obj = Student()

# Menu Driven Program
while True:

    print("\n===== STUDENT INFORMATION SYSTEM =====")
    print("1. Enter Student Details")
    print("2. Display Student Details")
    print("3. Display Student Grade")
    print("4. Exit")

    try:
        # Taking user choice
        choice = int(input("Enter Your Choice: "))

        # Call method to enter details
        if choice == 1:
            obj.get_data()

        # Call method to display details
        elif choice == 2:
            obj.display()

        # Call method to display grade
        elif choice == 3:
            obj.grade()

        # Exit the program
        elif choice == 4:
            print("Program Ended Successfully.")
            break

        # Invalid menu choice
        else:
            print("Invalid Choice! Please select between 1 and 4.")

    # Handle non-numeric input
    except ValueError:
        print("Invalid Input! Enter a number only.")
