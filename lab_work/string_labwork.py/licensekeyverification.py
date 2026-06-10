# Input license key
key = "ABCD-EFGH-IJKL-MNOP"

# Create list of groups
groups = key.split("-")

# Check validity
valid = True

if len(groups) != 4:
    valid = False

for group in groups:

    if len(group) != 4:
        valid = False

# Count letters and vowels
letters = 0
vowels = 0

for ch in key:

    if ch.isalpha():

        letters += 1

        if ch.upper() in "AEIOU":
            vowels += 1

# Remove hyphens
merged_key = key.replace("-", "")

# Display output
print("License Key:", key)
print("Groups:", groups)
print("Number of Groups:", len(groups))
print("Total Letters:", letters)
print("Total Vowels:", vowels)
print("Merged Key:", merged_key)

if valid:
    print("License Key Status: Valid")
else:
    print("License Key Status: Invalid")