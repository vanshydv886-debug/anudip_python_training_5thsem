#program for area of rectangle using class and object with methods and menu bar 
 class Rectangle:
    def __init__(self):
        self.length = 0
        self.breadth = 0

    def get_data(self):
        while True:
            try:
                self.length = float(input("Enter Length: "))
                self.breadth = float(input("Enter Breadth: "))

                if self.length <= 0 or self.breadth <= 0:
                    print("Length and Breadth must be greater than 0!")
                else:
                    break

            except ValueError:
                print("Invalid Input! Enter numeric values only.")

    def area(self):
        if self.length == 0 or self.breadth == 0:
            print("Please enter dimensions first.")
        else:
            print("Area of Rectangle =", self.length * self.breadth)

    def perimeter(self):
        if self.length == 0 or self.breadth == 0:
            print("Please enter dimensions first.")
        else:
            print("Perimeter of Rectangle =", 2 * (self.length + self.breadth))


obj = Rectangle()

while True:
    print("\n===== MENU =====")
    print("1. Enter Rectangle Dimensions")
    print("2. Calculate Area")
    print("3. Calculate Perimeter")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            obj.get_data()

        elif choice == 2:
            obj.area()

        elif choice == 3:
            obj.perimeter()

        elif choice == 4:
            print("Program Terminated.")
            break

        else:
            print("Invalid Choice! Please select between 1 and 4.")

    except ValueError:
        print("Invalid Input! Enter a number between 1 and 4.")