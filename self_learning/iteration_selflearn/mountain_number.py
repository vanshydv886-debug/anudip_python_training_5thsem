# Accept number
num = input("Enter Number: ")

i = 0

# Increasing part
while i < len(num) - 1 and num[i] < num[i + 1]:
    i += 1

# Decreasing part
while i < len(num) - 1 and num[i] > num[i + 1]:
    i += 1

# Check result
if i == len(num) - 1:
    print("Mountain Number")
else:
    print("Not a Mountain Number"