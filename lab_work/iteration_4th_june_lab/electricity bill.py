# Electricity Bill Calculator
# This program calculates bill based on units consumed

units = int(input("Enter electricity units consumed: "))

bill = 0  # initial bill value

# First slab: 0 - 100 units
if units <= 100:
    bill = units * 5

# Second slab: 101 - 200 units
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7

# Third slab: above 200 units
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Total Electricity Bill = ₹", bill)