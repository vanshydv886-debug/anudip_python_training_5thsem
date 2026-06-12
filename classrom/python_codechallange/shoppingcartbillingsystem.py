# program fo shopping car billing system
prices = (1250, 799, 450, 999, 300, 1500, 650, 250, 850, 1200) 
prices = (1250, 799, 450, 999, 300, 1500, 650, 250, 850, 1200)

# Total bill amount
total_bill = sum(prices)
print("Total Bill Amount: ₹", total_bill)

# Most expensive product
most_expensive = max(prices)
print("Most Expensive Product: ₹", most_expensive)

# Least expensive product
least_expensive = min(prices)
print("Least Expensive Product: ₹", least_expensive)

# Count products costing more than ₹1000
count = 0
for price in prices:
    if price > 1000:
        count += 1

print("Products Costing More Than ₹1000:", count)

# Products eligible for discount
discount_products = []

for price in prices:
    if price > 800:
        discount_products.append(price)

print("Products Eligible for Discount:", discount_products)