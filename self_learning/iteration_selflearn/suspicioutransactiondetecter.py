# Initialize counters
high_count = 0
low_count = 0
total = 0

while True:

    # Input transaction amount
    amount = int(input("Enter Transaction Amount (-1 to stop): "))

    # Stop condition
    if amount == -1:
        break

    # Add to total
    total += amount

    # Count transactions above 50000
    if amount > 50000:
        high_count += 1

    # Count transactions below 1000
    if amount < 1000:
        low_count += 1

# Display results
print("Transactions Above 50000:", high_count)
print("Transactions Below 1000:", low_count)
print("Total Transaction Amount:", total)