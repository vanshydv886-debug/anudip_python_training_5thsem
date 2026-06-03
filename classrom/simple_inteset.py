p = float(input("Enter Principal Amount: "))
if p <= 0:
    print("Invalid Principal Amount")
    exit()

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