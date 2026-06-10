# Vehicle Number Plate Verification

vehicle = "MH12AB4589"

print("Vehicle Number:", vehicle)

# 1. Extract State Code
state_code = vehicle[:2]
print("State Code:", state_code)

# 2. Extract District Code
district_code = vehicle[2:4]
print("District Code:", district_code)

# 3. Extract Vehicle Series
series = vehicle[4:6]
print("Series:", series)

# 4. Extract Vehicle Number
number = vehicle[6:]
print("Vehicle Number:", number)

# 5. Count Letters and Digits
letters = 0
digits = 0

for ch in vehicle:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("Total Letters:", letters)
print("Total Digits:", digits)

# 6. Verify Number Plate Format

if (vehicle[:2].isalpha() and
    vehicle[2:4].isdigit() and
    vehicle[4:6].isalpha() and
    vehicle[6:].isdigit() and
    len(vehicle) == 10):

    print("Vehicle Number Status: Valid")
else:
    print("Vehicle Number Status: Invalid")