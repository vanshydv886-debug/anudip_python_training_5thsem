#program for fooddelivery performmance dashboard
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# Fastest delivery
fastest = min(delivery_times)
print("Fastest Delivery:", fastest, "minutes")

# Slowest delivery
slowest = max(delivery_times)
print("Slowest Delivery:", slowest, "minutes")

# Average delivery time
average = sum(delivery_times) / len(delivery_times)
print("Average Delivery Time:", round(average, 1), "minutes")

# Delayed orders
delayed_orders = []

for time in delivery_times:
    if time > 45:
        delayed_orders.append(time)

print("Delayed Orders:", delayed_orders)

# Categorization
fast = 0
normal = 0
delayed = 0

for time in delivery_times:
    if time <= 30:
        fast += 1
    elif time <= 45:
        normal += 1
    else:
        delayed += 1

print("Fast Deliveries:", fast)
print("Normal Deliveries:", normal)
print("Delayed Deliveries:", delayed)