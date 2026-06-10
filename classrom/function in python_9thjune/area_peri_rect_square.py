import perimeter_rectangle
import perimeter_square
import perimeter_circle

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
print("Perimeter of Rectangle =", perimeter_rectangle.perimeter_rectangle(length, breadth))

side = int(input("Enter side: "))
print("Perimeter of Square =", perimeter_square.perimeter_square(side))

radius = int(input("Enter radius: "))
print("Circumference of Circle =", perimeter_circle.perimeter_circle(radius))