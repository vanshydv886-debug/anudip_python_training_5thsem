 # Input first angle
angle1 = float(input("Enter first angle: "))

# Validate first angle
if angle1 <= 0:
    exit("Angle must be positive")

# Input second angle
angle2 = float(input("Enter second angle: "))

# Validate second angle
if angle2 <= 0:
    exit("Angle must be positive")

# Input third angle
angle3 = float(input("Enter third angle: "))

# Validate third angle
if angle3 <= 0:
    exit("Angle must be positive")

# Verify whether the three angles can form a triangle
# Sum of all angles in a triangle must be 180 degrees
if angle1 + angle2 + angle3 == 180:
    print("Above angles form a triangle")
else:
    print("Above angles do not form a triangle")    