# Program to check whether a number is Prime or not using Flag

# Accept a number from the user
num = int(input("Enter a number: "))

# Assume the number is prime
flag = True

# Check if  number is less than or equal to 1
if num <= 1:
    flag = False

else:
    for i in range(2, num):

        # If the number is divisible by i,
        # then it is not a prime number
        if num % i == 0:
            flag = False
            break   # Exit the loop immediately

# for result
if flag:
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")
