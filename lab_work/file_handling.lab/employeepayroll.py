def read_employees():
    employees = []

    f = open("employees.txt", "r")

    for line in f:
        empid, name, salary = line.strip().split(",")
        employees.append([empid, name, int(salary)])

    f.close()
    return employees


while True:

    print("\n----- Employee Payroll Management System -----")
    print("1. Display all employee records")
    print("2. Search employee by ID")
    print("3. Calculate average salary")
    print("4. Highest-paid and lowest-paid employee")
    print("5. Employees earning above 50000")
    print("6. Add new employee")
    print("7. Salary categories")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    employees = read_employees()

    if choice == 1:

        print("\nEmployee Records")
        for emp in employees:
            print(emp[0], emp[1], emp[2])

    elif choice == 2:

        search_id = input("Enter Employee ID: ")

        found = False

        for emp in employees:
            if emp[0] == search_id:
                print("ID:", emp[0])
                print("Name:", emp[1])
                print("Salary:", emp[2])
                found = True
                break

        if not found:
            print("Employee not found")

    elif choice == 3:

        total = 0

        for emp in employees:
            total += emp[2]

        average = total / len(employees)

        print("Average Salary =", average)

    elif choice == 4:

        highest = employees[0]
        lowest = employees[0]

        for emp in employees:

            if emp[2] > highest[2]:
                highest = emp

            if emp[2] < lowest[2]:
                lowest = emp

        print("Highest Paid Employee:")
        print(highest[0], highest[1], highest[2])

        print("Lowest Paid Employee:")
        print(lowest[0], lowest[1], lowest[2])

    elif choice == 5:

        print("Employees earning above 50000")

        for emp in employees:
            if emp[2] > 50000:
                print(emp[0], emp[1], emp[2])

    elif choice == 6:

        empid = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        salary = input("Enter Salary: ")

        f = open("employees.txt", "a")
        f.write("\n" + empid + "," + name + "," + salary)
        f.close()

        print("Employee added successfully")

    elif choice == 7:

        print("\nSalary Categories")

        for emp in employees:

            if emp[2] >= 60000:
                category = "High"

            elif emp[2] >= 40000:
                category = "Medium"

            else:
                category = "Low"

            print(emp[0], emp[1], emp[2], "-", category)

    elif choice == 8:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")