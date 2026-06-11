# Function to read expenses from file
def read_expenses():

    expenses = []

    f = open("expenses.txt", "r")

    for line in f:

        category, amount = line.strip().split(",")

        expenses.append([category, int(amount)])

    f.close()

    return expenses


# Function to save updated expenses
def save_expenses(expenses):

    f = open("expenses.txt", "w")

    for expense in expenses:

        f.write(expense[0] + "," + str(expense[1]) + "\n")

    f.close()


# Function to display all expenses
def display_expenses():

    expenses = read_expenses()

    print("\nExpense Records")

    for expense in expenses:

        print(expense[0], "-", expense[1])


# Function to calculate total expenditure
def total_expense():

    expenses = read_expenses()

    total = 0

    for expense in expenses:

        total += expense[1]

    print("Total Expenditure =", total)


# Function to find highest and lowest expense
def highest_lowest():

    expenses = read_expenses()

    highest = expenses[0]
    lowest = expenses[0]

    for expense in expenses:

        if expense[1] > highest[1]:
            highest = expense

        if expense[1] < lowest[1]:
            lowest = expense

    print("Highest Expense =", highest[0], highest[1])
    print("Lowest Expense =", lowest[0], lowest[1])


# Function to display expenses greater than 800
def expenses_above_800():

    expenses = read_expenses()

    print("\nExpenses Greater Than 800")

    for expense in expenses:

        if expense[1] > 800:

            print(expense[0], "-", expense[1])


# Function to add new expense category
def add_expense():

    expenses = read_expenses()

    category = input("Enter Category: ")
    amount = int(input("Enter Amount: "))

    expenses.append([category, amount])

    save_expenses(expenses)

    print("Expense Added Successfully")


# Function to update expense amount
def update_expense():

    expenses = read_expenses()

    category = input("Enter Category to Update: ")

    found = False

    for expense in expenses:

        if expense[0].lower() == category.lower():

            amount = int(input("Enter New Amount: "))

            expense[1] = amount

            found = True

            print("Expense Updated")

    if found == False:

        print("Category Not Found")

    save_expenses(expenses)


# Function to generate report.txt
def generate_report():

    expenses = read_expenses()

    total = 0

    highest = expenses[0]
    lowest = expenses[0]

    for expense in expenses:

        total += expense[1]

        if expense[1] > highest[1]:
            highest = expense

        if expense[1] < lowest[1]:
            lowest = expense

    r = open("report.txt", "w")

    r.write("TOTAL EXPENSES = " + str(total) + "\n")
    r.write("HIGHEST EXPENSE = " + highest[0] + "\n")
    r.write("LOWEST EXPENSE = " + lowest[0] + "\n")

    r.write("\nCATEGORIES ABOVE 800\n")

    for expense in expenses:

        if expense[1] > 800:

            r.write(expense[0] + " - " + str(expense[1]) + "\n")

    r.close()

    print("report.txt created successfully")


# Main Menu
while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Display Expenses")
    print("2. Total Expenditure")
    print("3. Highest and Lowest Expense")
    print("4. Expenses Greater Than 800")
    print("5. Add Expense Category")
    print("6. Update Expense Amount")
    print("7. Generate Report")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        display_expenses()

    elif choice == 2:
        total_expense()

    elif choice == 3:
        highest_lowest()

    elif choice == 4:
        expenses_above_800()

    elif choice == 5:
        add_expense()

    elif choice == 6:
        update_expense()

    elif choice == 7:
        generate_report()

    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")