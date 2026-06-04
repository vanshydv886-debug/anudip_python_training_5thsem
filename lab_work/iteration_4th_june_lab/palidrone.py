# Palindrome and Reverse Number Checker
# A number is palindrome if reverse is same as original

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10          # extract last digit
    reverse = reverse * 10 + digit  # build reverse number
    num = num // 10           # remove last digit

    print("Reverse Number =", reverse)

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")