# Password Strength Analyzer

# Storing password
password = "Python@2026!"

# Counters
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

# Lists to store digits and special characters
digits_found = []
special_found = []

# Traversing each character of password
for ch in password:

    # Check for uppercase letters
    if ch.isupper():
        upper_count += 1

    # Check for lowercase letters
    elif ch.islower():         #small letter
        lower_count += 1

    # Check for digits
    elif ch.isdigit():
        digit_count += 1
        digits_found.append(ch)

    # Remaining characters are special characters
    else:
        special_count += 1
        special_found.append(ch)

# Checking password strength

# Strong Password Conditions:
# 1. Length >= 8
# 2. At least 1 uppercase letter
# 3. At least 1 lowercase letter
# 4. At least 1 digit
# 5. At least 1 special character

if (len(password) >= 8 and
    upper_count >= 1 and
    lower_count >= 1 and
    digit_count >= 1 and
    special_count >= 1):

    strength = "Strong"

# If length is okay but all conditions are not satisfied
elif len(password) >= 8:
    strength = "Medium"

# If length is less than 8
else:
    strength = "Weak"

# Displaying results
print("Password:", password)

print("\nUppercase Letters:", upper_count)
print("Lowercase Letters:", lower_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)

print("\nDigits Found:", digits_found)
print("Special Characters Found:", special_found)

print("\nPassword Strength:", strength)