#program to area and perimeter of a rectangle
#input of length and breadth
length=int(input("enter the length of rectangle"))
if(length<0):
    exit("Length cannot be negative")
breadth=int(input("enter the breadth of the retangle: "))
if(breadth<0):
    exit("Breadth cannot be negative")
print("Area of the rectangle is: " , length*breadth)
print("perimeter of the rectangle is: ", 2*(length+breadth))