# E-Commerce Inventory & Sales Dashboard

# Dictionary containing product details
products = {
    "P101": {"name": "Laptop", "price": 55000, "stock": 12, "sold": 25},
    "P102": {"name": "Mobile", "price": 25000, "stock": 8, "sold": 40},
    "P103": {"name": "Headphones", "price": 2000, "stock": 5, "sold": 15},
    "P104": {"name": "Keyboard", "price": 1500, "stock": 3, "sold": 8},
    "P105": {"name": "Mouse", "price": 800, "stock": 0, "sold": 20}
}

while True:

    # Display menu
    print("\n===== E-COMMERCE INVENTORY & SALES DASHBOARD =====")
    print("1. Display all products")
    print("2. Add a new product")
    print("3. Update stock after sales")
    print("4. Find out-of-stock products")
    print("5. Find products with stock less than 5")
    print("6. Calculate total inventory value")
    print("7. Find best-selling product")
    print("8. Find least-selling product")
    print("9. Calculate total revenue generated")
    print("10. Generate low-stock report")
    print("11. Display products whose sales exceed average sales")
    print("12. Create promotion products dictionary")
    print("13. Generate complete business report")
    print("14. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Display all products
    if choice == 1:

        print("\nAll Products:")
        for pid, data in products.items():
            print(pid, data)

    # 2. Add a new product
    elif choice == 2:

        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        price = int(input("Enter Price: "))
        stock = int(input("Enter Stock: "))
        sold = int(input("Enter Sold Quantity: "))

        products[pid] = {
            "name": name,
            "price": price,
            "stock": stock,
            "sold": sold
        }

        print("Product Added Successfully")

    # 3. Update stock after sales
    elif choice == 3:

        pid = input("Enter Product ID: ")

        if pid in products:

            qty = int(input("Enter Quantity Sold: "))

            products[pid]["stock"] -= qty
            products[pid]["sold"] += qty

            print("Stock Updated Successfully")

        else:
            print("Product Not Found")

    # 4. Find out-of-stock products
    elif choice == 4:

        print("\nOut Of Stock Products:")

        for pid, data in products.items():

            if data["stock"] == 0:
                print(pid, data)

    # 5. Find products with stock less than 5
    elif choice == 5:

        print("\nProducts With Stock Less Than 5:")

        for pid, data in products.items():

            if data["stock"] < 5:
                print(pid, data)

    # 6. Calculate total inventory value
    elif choice == 6:

        inventory_value = 0

        for data in products.values():

            inventory_value += data["price"] * data["stock"]

        print("Total Inventory Value =", inventory_value)

    # 7. Find best-selling product
    elif choice == 7:

        best_product = ""
        highest_sales = -1

        for pid, data in products.items():

            if data["sold"] > highest_sales:

                highest_sales = data["sold"]
                best_product = pid

        print("Best Selling Product =", best_product)
        print(products[best_product])

    # 8. Find least-selling product
    elif choice == 8:

        least_product = ""
        lowest_sales = 999999

        for pid, data in products.items():

            if data["sold"] < lowest_sales:

                lowest_sales = data["sold"]
                least_product = pid

        print("Least Selling Product =", least_product)
        print(products[least_product])

    # 9. Calculate total revenue generated
    elif choice == 9:

        revenue = 0

        for data in products.values():

            revenue += data["price"] * data["sold"]

        print("Total Revenue Generated =", revenue)

    # 10. Generate low-stock report
    elif choice == 10:

        print("\nLOW STOCK REPORT")

        for pid, data in products.items():

            if data["stock"] < 5:

                print(pid, data["name"], "Stock =", data["stock"])

    # 11. Products whose sales exceed average sales
    elif choice == 11:

        total_sales = 0

        for data in products.values():

            total_sales += data["sold"]

        average_sales = total_sales / len(products)

        print("Average Sales =", average_sales)

        print("\nProducts Above Average Sales:")

        for pid, data in products.items():

            if data["sold"] > average_sales:

                print(pid, data)

    # 12. Create promotion products dictionary
    elif choice == 12:

        promotion = {}

        for pid, data in products.items():

            if data["sold"] < 10:

                promotion[pid] = data

        print("\nPromotion Eligible Products:")
        print(promotion)

    # 13. Generate complete business report
    elif choice == 13:

        inventory_value = 0
        revenue = 0

        for data in products.values():

            inventory_value += data["price"] * data["stock"]
            revenue += data["price"] * data["sold"]

        best_product = ""
        highest_sales = -1

        least_product = ""
        lowest_sales = 999999

        for pid, data in products.items():

            if data["sold"] > highest_sales:

                highest_sales = data["sold"]
                best_product = pid

            if data["sold"] < lowest_sales:

                lowest_sales = data["sold"]
                least_product = pid

        promotion_count = 0

        for data in products.values():

            if data["sold"] < 10:
                promotion_count += 1

        print("\n===== COMPLETE BUSINESS REPORT =====")
        print("Total Products =", len(products))
        print("Inventory Value =", inventory_value)
        print("Revenue Generated =", revenue)
        print("Best Selling Product =", best_product)
        print("Least Selling Product =", least_product)
        print("Promotion Eligible Products =", promotion_count)

    # 14. Exit
    elif choice == 14:

        print("Program Ended Successfully")
        break

    else:
        print("Invalid Choice")