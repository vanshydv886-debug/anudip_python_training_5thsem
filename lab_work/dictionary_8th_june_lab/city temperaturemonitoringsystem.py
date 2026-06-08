temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# 1. Cities having temperature above 40°C
print("Cities Having Temperature Above 40°C:")

for city, temp in temperature.items():
    if temp > 40:
        print(city)

# 2. Hottest City
hottest_city = max(temperature, key=temperature.get)

print("\nHottest City:", hottest_city,
      "(", temperature[hottest_city], "°C)", sep="")

# 3. Coolest City
coolest_city = min(temperature, key=temperature.get)

print("Coolest City:", coolest_city,
      "(", temperature[coolest_city], "°C)", sep="")

# 4. Average Temperature
average = sum(temperature.values()) / len(temperature)

print("Average Temperature:", round(average, 1), "°C")

# 5. Pleasant Cities
pleasant = []

for city, temp in temperature.items():
    if temp < 35:
        pleasant.append(city)

print("Pleasant Cities:", pleasant)

# 6. Count cities with temperature between 35°C and 40°C
count = 0

for temp in temperature.values():
    if 35 <= temp <= 40:
        count += 1

print("Cities with Temperature Between 35°C and 40°C:", count)