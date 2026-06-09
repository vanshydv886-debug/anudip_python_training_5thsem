rows = int(input("Enter the number of rows: "))

if(rows <= 0):
    exit("Invalid number of rows")

for i in range(1, rows + 1):
    print("*" * i)