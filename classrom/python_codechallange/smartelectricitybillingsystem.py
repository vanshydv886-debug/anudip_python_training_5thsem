# program for smart electricity bill
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

#for house consuming more than 400 units
print("Houses consuming more than 400 units:")
for house, unit in units.items():
    if unit > 400:
        print(house, ":", unit)

#highest and lowest consuming house 
highest_house = max(units, key=units.get)
lowest_house = min(units, key=units.get)

print("\nHighest Consuming House:")
print(highest_house, ":", units[highest_house])

print("\nLowest Consuming House:")
print(lowest_house, ":", units[lowest_house])

total_units = sum(units.values())
print("\nTotal Units Consumed =", total_units)

low = []
medium = []
high = []

for house, unit in units.items():
    if unit < 200:
        low.append(house)
    elif 200 <= unit <= 400:
        medium.append(house)
    else:
        high.append(house)

print("\nLow Consumption (<200):")
print(low)

print("\nMedium Consumption (200-400):")
print(medium)

print("\nHigh Consumption (>400):")
print(high)

campaign_count = 0

for unit in units.values():
    if unit > 300:
        campaign_count += 1

print("\nHouses eligible for Energy-Saving Campaign =", campaign_count)