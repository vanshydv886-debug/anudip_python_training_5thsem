Delivery times (in minutes) for different orders are given below: delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] Requirements Create the following functions: 1. fastest_delivery(times) Returns the shortest delivery time. 2. delayed_orders(times) Returns a list of orders taking more than 45 minutes. 3. average_delivery_time(times) Returns the average delivery time. 4. delivery_category(times) Displays order categories: • Fast → ≤ 30 minutes  • Normal → 31–45 minutes  • Delayed → > 45 minutes  

#program for food delivery tracker
# List of delivery times
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# Function to find fastest delivery
def fastest_delivery(times):

    fastest = min(times)

    print("Fastest Delivery Time =", fastest)


# Function to find delayed orders
def delayed_orders(times):

    delayed = []

    for i in times:

        if i > 45:
            delayed.append(i)

    print("Delayed Orders =", delayed)


# Function to calculate average delivery time
def average_delivery_time(times):

    average = sum(times) / len(times)

    print("Average Delivery Time =", average)


# Function to display delivery category
def delivery_category(times):

    for i in times:

        if i <= 30:
            print(i, "-> Fast")

        elif i <= 45:
            print(i, "-> Normal")

        else:
            print(i, "-> Delayed")


# Function Calls
fastest_delivery(delivery_time)
delayed_orders(delivery_time)
average_delivery_time(delivery_time)
delivery_category(delivery_time)