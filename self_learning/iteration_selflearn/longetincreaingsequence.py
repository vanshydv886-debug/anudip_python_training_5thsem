# Input total numbers
n = int(input("Enter N: "))

# Read first number
prev = int(input("Enter Number: "))

# Initialize sequence lengths
max_len = 1
curr_len = 1

# Read remaining numbers
for i in range(n - 1):

    num = int(input("Enter Number: "))

    # Check increasing sequence
    if num > prev:
        curr_len += 1

    else:
        # Update maximum length
        if curr_len > max_len:
            max_len = curr_len

        curr_len = 1

    prev = num

# Final check
if curr_len > max_len:
    max_len = curr_len

print("Longest Sequence Length =", max_len)