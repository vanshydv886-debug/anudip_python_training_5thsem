# Input number of racers
n = int(input("Enter Number of Racers: "))

times = []

# Input lap times
for i in range(n):

    lap = int(input(f"Lap Time of Racer {i+1}: "))
    times.append(lap)

# Find fastest and slowest times
fastest = min(times)
slowest = max(times)

# Display results
print("Fastest Racer Position:", times.index(fastest) + 1)
print("Slowest Racer Position:", times.index(slowest) + 1)
print("Difference:", slowest - fastest)