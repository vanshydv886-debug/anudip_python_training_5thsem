 # Employee ID Validation and Analysis System

emp_id = "EMP2026ANUJ458"

# Task 1 & 2: Count uppercase letters and digits
upper_count = 0
digit_count = 0

for ch in emp_id:
    if ch.isupper():
        upper_count += 1
    elif ch.isdigit():
        digit_count += 1

print("Employee ID:", emp_id)
print("\nUppercase Letters:", upper_count)
print("Digits:", digit_count)

# Task 3: Extract joining year
joining_year = emp_id[3:7]
print("\nJoining Year:", joining_year)

# Task 4: Extract employee name
employee_name = emp_id[7:-3]
print("Employee Name:", employee_name)

# Task 5: Validate ID Format
valid = True

# Rule 1: Starts with EMP
if not emp_id.startswith("EMP"):
    valid = False

# Rule 2: Year must be exactly 4 digits
if not emp_id[3:7].isdigit():
    valid = False

# Rule 3: Ends with exactly 3 digits
if not emp_id[-3:].isdigit():
    valid = False

# Task 6 & 7: Create digit list and sum of digits
digit_list = []
digit_sum = 0

for ch in emp_id:
    if ch.isdigit():
        digit_list.append(int(ch))
        digit_sum += int(ch)

print("\nDigit List:", digit_list)
print("Sum of Digits:", digit_sum)

# Task 8: Display ID Status
if valid:
    print("\nID Status: Valid")
else:
    print("\nID Status: Invalid")

