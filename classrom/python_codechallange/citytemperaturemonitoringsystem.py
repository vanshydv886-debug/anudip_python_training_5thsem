# program for city moniotoring temperature system
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

print("Cities Above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)

hottest = max(temperature, key=temperature.get)
print("\nHottest City:", hottest, "(", temperature[hottest], "°C)", sep="")

coolest = min(temperature, key=temperature.get)
print("Coolest City:", coolest, "(", temperature[coolest], "°C)", sep="")

average = sum(temperature.values()) / len(temperature)
print("Average Temperature:", round(average, 1), "°C")

pleasant = []

for city, temp in temperature.items():
    if temp < 35:
        pleasant.append(city)

print("Pleasant Cities:", pleasant)