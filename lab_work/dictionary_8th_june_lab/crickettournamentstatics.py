runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# 1. Players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")

for player, run in runs.items():
    if run > 500:
        print(player)

# 2. Orange Cap Winner
orange_cap = max(runs, key=runs.get)

print("\nOrange Cap Winner:", orange_cap,
      "(", runs[orange_cap], ")", sep="")

# 3. Lowest Scorer
lowest_scorer = min(runs, key=runs.get)

print("Lowest Scorer:", lowest_scorer,
      "(", runs[lowest_scorer], ")", sep="")

# 4. Total Tournament Runs
total_runs = sum(runs.values())

print("Total Tournament Runs:", total_runs)

# 5. Players Scoring Below 400
below_400 = []

for player, run in runs.items():
    if run < 400:
        below_400.append(player)

print("Players Scoring Below 400:", below_400)

# 6. Players Between 400 and 600 Runs
count = 0

for run in runs.values():
    if 400 <= run <= 600:
        count += 1

print("Players Between 400 and 600 Runs:", count)