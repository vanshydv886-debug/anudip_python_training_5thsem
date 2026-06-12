# program for onlineshopping invontery system 
inventory = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

print("Products with Stock Below 15:")
for product, stock in inventory.items():
    if stock < 15:g
        print(product)

highest = max(inventory, key=inventory.get)
print("\nHighest Stock Product:", highest, "(", inventory[highest], "units)", sep="")

lowest = min(inventory, key=inventory.get)
print("Lowest Stock Product:", lowest, "(", inventory[lowest], "units)", sep="")

total_stock = sum(inventory.values())
print("Total Stock Available:", total_stock)

restocking = []

for product, stock in inventory.items():
    if stock < 10:
        restocking.append(product)

print("Products Requiring Restocking:", restocking)