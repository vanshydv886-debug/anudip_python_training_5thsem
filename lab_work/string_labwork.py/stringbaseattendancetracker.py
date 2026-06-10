# Attendance record
attendance = "PPAPPPAAPPPPAPP"

# Count present and absent days
present = attendance.count("P")
absent = attendance.count("A")

# Calculate attendance percentage
percentage = (present / len(attendance)) * 100

# Longest present streak
max_present = 0
current_present = 0

for ch in attendance:

    if ch == "P":
        current_present += 1

        if current_present > max_present:
            max_present = current_present

    else:
        current_present = 0

# Longest absent streak
max_absent = 0
current_absent = 0

for ch in attendance:

    if ch == "A":
        current_absent += 1

        if current_absent > max_absent:
            max_absent = current_absent

    else:
        current_absent = 0

# Attendance status
if percentage < 75:
    status = "Below 75%"
else:
    status = "Above 75%"

# Display output
print("Attendance Record:", attendance)
print("Present Days:", present)
print("Absent Days:", absent)
print("Attendance Percentage:", round(percentage, 2), "%")
print("Longest Present Streak:", max_present)
print("Longest Absent Streak:", max_absent)
print("Attendance Status:", status)