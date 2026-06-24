# Input number
num = input("Enter Number: ")

# Find middle position
mid = len(num) // 2

# Divide number into two halves
left = num[:mid]
right = num[mid:]

# Compare both halves
if left == right:
    print("Mirror Number")
else:
    print("Not a Mirror Number")