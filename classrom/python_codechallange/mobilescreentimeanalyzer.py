#program for mobile screen time analyzer
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260]

# Average screen time
average = sum(screen_time) / len(screen_time)
print("Average Screen Time:", round(average, 1), "minutes")

# Highest and Lowest screen time
highest = max(screen_time)
lowest = min(screen_time)

print("Highest Screen Time:", highest, "minutes")
print("Lowest Screen Time:", lowest, "minutes")

# Days exceeding 200 minutes
count = 0
for time in screen_time:
    if time > 200:
        count += 1

print("Days Exceeding 200 Minutes:", count)

# Healthy usage days
print("Healthy Usage Days:")
for i in range(len(screen_time)):
    if screen_time[i] < 180:
        print("Day", i + 1)

# Categorization
healthy = 0
moderate = 0
excessive = 0

for time in screen_time:
    if time < 180:
        healthy += 1
    elif time <= 240:
        moderate += 1
    else:
        excessive += 1

print("Healthy:", healthy)
print("Moderate:", moderate)
print("Excessive:", excessive)