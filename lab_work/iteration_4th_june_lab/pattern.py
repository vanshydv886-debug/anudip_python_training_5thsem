# Accept number of rows
rows = int(input("Enter number of rows: "))

# Print Number Pyramid
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Print Reverse Pattern
print("\nReverse Pattern:")

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()