# Input name
name = input("Enter Name: ")

# Remove spaces
username = name.replace(" ", "")

# Convert to lowercase
username = username.lower()

# Append current year
username = username + "2026"

# Limit username to 12 characters if needed
if len(username) > 12:
    username = username[:12]

# Count vowels and consonants
vowels = 0
consonants = 0

for ch in username:

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1

        else:
            consonants += 1

# Display output
print("Original Name:", name)
print("Generated Username:", username)
print("Username Length:", len(username))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Status: Username Generated Successfully")