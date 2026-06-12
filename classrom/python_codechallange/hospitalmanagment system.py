#program for hospital patient moniotoring system
heart_rate = {
    "P101": 72,
    "P102": 105,
    "P103": 88,
    "P104": 120,
    "P105": 65,
    "P106": 98,
    "P107": 110,
    "P108": 70,
    "P109": 85,
    "P110": 130
}

print("Critical Patients:")
for patient, rate in heart_rate.items():
    if rate > 100:
        print(patient)

highest = max(heart_rate, key=heart_rate.get)
print("\nHighest Heart Rate:")
print(highest, "(", heart_rate[highest], "bpm)", sep="")

lowest = min(heart_rate, key=heart_rate.get)
print("\nLowest Heart Rate:")
print(lowest, "(", heart_rate[lowest], "bpm)", sep="")

average = sum(heart_rate.values()) / len(heart_rate)
print("\nAverage Heart Rate:", round(average, 1), "bpm")

stable_count = 0

for rate in heart_rate.values():
    if 60 <= rate <= 100:
        stable_count += 1

print("Stable Patients:", stable_count)