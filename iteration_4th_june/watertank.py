# Water Tank Filling Program
# Tank fills at 10 liters per minute
# Initial water level is 0 liters

water = 0

# Continue until tank reaches 100 liters
while water < 100:
    water = water + 10  # increase water level by 10 liters each minute
    print("Water Level:", water, "liters")

print("Tank is full.")