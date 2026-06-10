import perimeter_rectangle 

while True:
    print("\n===== MENU =====")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        length = int(input("Enter length: "))
        breadth = int(input("Enter breadth: "))

        result = perimeter_rectangle.perimeter_rectangle(length, breadth)
        print("Perimeter of Rectangle =", result)

    elif choice == 2:
        side = int(input("Enter side: "))

        result = perimeter_square.perimeter_square(side)
        print("Perimeter of Square =", result)

    elif choice == 3:
        radius = int(input("Enter radius: "))

        result = perimeter_circle.perimeter_circle(radius)
        print("Circumference of Circle =", result)

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")