# Strong Number (Easy Version)

num = int(input("Enter number: "))

temp = num
total = 0

while temp > 0:
    digit = temp % 10

    # factorial of digit (simple loop)
    fact = 1
    i = 1

    while i <= digit:
        fact *= i
        i += 1

    total += fact
    temp //= 10

if total == num:
    print("Strong Number")
else:
    print("Not Strong Number")