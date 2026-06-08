#online shoping order analytics

sales = {     "Laptop": 15,     "Mouse": 45,     "Keyboard": 32,     "Monitor": 12,     "Headphones": 28,     "Printer": 8,     "Webcam": 20,     "Speaker": 18,     "Tablet": 10,     "Router": 25 } 

#display product sod more than 20 times 
print("products sold more than 20 times ")
for product quantity in sales_items:
    if quantity > 20 :
        print(product)

#best selling product
best_product = max(sales, key=sales.get)
print("\nBest Selling Product:", best_product, "(", sales[best_product], ")", sep="")  

#least sellig product
least_product = min(sales, key=sales.get)
print("\nleast Selling Product:", least_product, "(", sales[least_product], ")", sep="")  

# 4. Total products sold
total_sold = sum(sales.values())
print("Total Units Sold:", total_sold)

# 5. Products requiring promotion
promotion = []

for product, quantity in sales.items():
    if quantity < 15:
        promotion.append(product)

print("Products Requiring Promotion:", promotion)

# 6. Products having sales between 10 and 30
count = 0

for quantity in sales.values():
    if 10 <= quantity <= 30:
        count += 1

print("Products Having Sales Between 10 and 30:", count)