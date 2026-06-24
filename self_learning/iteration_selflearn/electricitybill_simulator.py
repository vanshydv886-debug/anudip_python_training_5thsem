# Input electricity units
units = int(input("Enter Units: "))

# Calculate bill according to slabs
if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Add surcharge if bill exceeds 5000
if bill > 5000:
    bill = bill + (bill * 0.10)

# Display final amount
print("Final Payable Amount =", bill)