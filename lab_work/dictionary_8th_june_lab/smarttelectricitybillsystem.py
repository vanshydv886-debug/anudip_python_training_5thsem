units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# 1. Houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")

for house, consumption in units.items():
    if consumption > 400:
        print(house)

# 2. Highest-consuming house
highest = max(units, key=units.get)

print("\nHighest Consumption:", highest,
      "(", units[highest], " units)", sep="")

# 3. Lowest-consuming house
lowest = min(units, key=units.get)

print("Lowest Consumption:", lowest,
      "(", units[lowest], " units)", sep="")

# 4. Total units consumed
total_units = sum(units.values())

print("Total Units Consumed:", total_units)

# 5. Consumption Categories
low = []
medium = []
high = []

for house, consumption in units.items():

    if consumption < 200:
        low.append(house)

    elif 200 <= consumption <= 400:
        medium.append(house)

    else:
        high.append(house)

print("Low Consumption:", low)
print("Medium Consumption:", medium)
print("High Consumption:", high)

# 6. Energy-saving campaign
count = 0

for consumption in units.values():
    if consumption > 300:
        count += 1

print("Eligible for Energy-Saving Campaign:", count)