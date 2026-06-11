import math # it use to calclate square root function sqrt()

try:
    # Input the lengths of the three sides of the triangle
    a = float(input("Enter the length of first side: "))
    b = float(input("Enter the length of second side: "))
    c = float(input("Enter the length of third side: "))

    # Check whether all sides are greater than zero
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Triangle sides must be greater than zero.")

    # Check Triangle Inequality Theorem
    # Sum of any two sides must be greater than the third side
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("Invalid triangle. The given sides cannot form a triangle.")

    # Calculate semi-perimeter using Heron's Formula
    s = (a + b + c) / 2

    # Calculate area of triangle
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Display the calculated area
    print("Area of the triangle =", round(area, 2))

# Handles non-numeric input and custom validation errors
except ValueError as e:
    print("Error:", e)

# Handles any other unexpected errors
except Exception:
    print("An unexpected error occurred.")

# Executes whether an exception occurs or not
finally:
    print("Triangle area calculation process completed.")