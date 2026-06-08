#program for stack inventory alert system 
# List contain stock quantities of products
stock = [25, 5, 0, 12, 3, 18, 0, 30]

out_of_stock = 0
available_products = 0

# List to store products that need restocking
restock_required = []

# List to store products with healthy stock
healthy_stock = []

# Traverse each stock quantity in the list
for quantity in stock:

    # Check if product is out of stock
    if quantity == 0:
        out_of_stock += 1

    # Check if product needs restocking
    if quantity < 10:
        restock_required.append(quantity)

    # Count available products
    if quantity > 0:
        available_products += 1

    # Create list of products with healthy stock
    if quantity >= 15:
        healthy_stock.append(quantity)

# Display the results
print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock_required)
print("Available Products:", available_products)
print("Healthy Stock:", healthy_stock)