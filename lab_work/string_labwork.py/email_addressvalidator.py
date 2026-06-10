# program for emailadress validator

# Input email
email = input("Enter Email: ")

# Extract username
username = email.split("@")[0]

# Extract domain and extension
domain_part = email.split("@")[1]

domain = domain_part.split(".")[0]
extension = domain_part.split(".")[1]

# Count digits in username
digit_count = 0

for ch in username:

    if ch.isdigit():
        digit_count += 1

# Count special characters
special_count = 0

for ch in email:

    if not ch.isalnum():
        special_count += 1

# Check validity
if email.count("@") == 1 and "." in domain_part:
    status = "Valid"
else:
    status = "Invalid"

# Display Output
print("Email:", email)
print("Username:", username)
print("Domain:", domain)
print("Extension:", extension)
print("Digits Found:", digit_count)
print("Special Characters Found:", special_count)
print("Email Status:", status)