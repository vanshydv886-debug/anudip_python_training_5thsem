#employer performance dashboard

performance = {     "EMP101": 92,     "EMP102": 78,     "EMP103": 45,     "EMP104": 88,     "EMP105": 97,     "EMP106": 56,     "EMP107": 81,     "EMP108": 64,     "EMP109": 39,     "EMP110": 73 } 

#display score more than 80
print("employes sccore more than 80 ")
for id , score in performance.items() :
    if score > 80:
        print(id)

 
# 2. Count employees needing improvement
count = 0

for score in performance.values():
    if score < 60:
        count += 1

print("\nEmployees Needing Improvement:", count)

# 3. Top Performer
top_performer = max(performance, key=performance.get)

print("Top Performer:", top_performer,
      "(", performance[top_performer], ")", sep="")

# 4. Average Performance Score
average = sum(performance.values()) / len(performance)

print("Average Score:", round(average, 1))

# 5. Employee Categories
excellent = []
good = []
average_list = []
poor = []

for emp_id, score in performance.items():

    if score >= 90:
        excellent.append(emp_id)

    elif 75 <= score <= 89:
        good.append(emp_id)

    elif 60 <= score <= 74:
        average_list.append(emp_id)

    else:
        poor.append(emp_id)

print("Excellent:", excellent)
print("Good:", good)
print("Average:", average_list)
print("Poor:", poor)