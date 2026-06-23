p = float(input("Enter Principal Amount: "))
if p <= 0:
    print("Invalid Principal Amount")
    exit()     #we have taken exit beacuse age p is negative baki 2 term positive theen answer is negative but si cannot be negative

r = float(input("Enter Rate of Interest: "))
if r <= 0:
    print("Invalid Rate of Interest")
    exit()

t = float(input("Enter Time (in years): "))
if t <= 0:
    print("Invalid Time")
    exit()

si = (p * r * t) / 100

print("Simple Interest =", si) 