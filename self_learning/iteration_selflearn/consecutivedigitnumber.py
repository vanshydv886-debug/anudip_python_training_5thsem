 # Accept number as string
num = input("Enter Number: ")

flag = True

# Check consecutive digits
for i in range(len(num) - 1):

    if int(num[i + 1]) != int(num[i]) + 1:
        flag = False
        break

# Display result
if flag:
    print("Consecutive Number")
else:
    print("Not a Consecutive Number")