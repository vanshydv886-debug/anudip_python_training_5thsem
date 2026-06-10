# City Population & Development Dashboard

cities = {
    "Delhi": {"population": 32000000, "area": 1484, "literacy": 89},
    "Mumbai": {"population": 21000000, "area": 603, "literacy": 91},
    "Kolkata": {"population": 15000000, "area": 205, "literacy": 88},
    "Chennai": {"population": 11000000, "area": 426, "literacy": 92},
    "Bangalore": {"population": 13000000, "area": 741, "literacy": 90}
}

while True:

    print("\n===== CITY POPULATION & DEVELOPMENT DASHBOARD =====")
    print("1. Display all city details")
    print("2. Most populated city")
    print("3. Least populated city")
    print("4. Average population")
    print("5. Cities with literacy above 90%")
    print("6. Cities with literacy below average")
    print("7. Calculate population density")
    print("8. City with highest density")
    print("9. Categorize cities")
    print("10. Development Priority List")
    print("11. High Literacy & Low Literacy Dictionaries")
    print("12. National Summary Report")
    print("13. Rank Cities by Density")
    print("14. Exit")

    choice = int(input("Enter choice: "))

    # 1. Display all city details
    if choice == 1:

        for city, data in cities.items():
            print(city, data)

    # 2. Most populated city
    elif choice == 2:

        max_city = ""
        max_pop = -1

        for city, data in cities.items():

            if data["population"] > max_pop:
                max_pop = data["population"]
                max_city = city

        print("Most Populated City =", max_city)
        print(cities[max_city])

    # 3. Least populated city
    elif choice == 3:

        min_city = ""
        min_pop = 999999999999

        for city, data in cities.items():

            if data["population"] < min_pop:
                min_pop = data["population"]
                min_city = city

        print("Least Populated City =", min_city)
        print(cities[min_city])

    # 4. Average population
    elif choice == 4:

        total_population = 0

        for data in cities.values():
            total_population += data["population"]

        average_population = total_population / len(cities)

        print("Average Population =", average_population)

    # 5. Literacy above 90%
    elif choice == 5:

        print("Cities With Literacy Above 90%")

        for city, data in cities.items():

            if data["literacy"] > 90:
                print(city, data)

    # 6. Literacy below average
    elif choice == 6:

        total_literacy = 0

        for data in cities.values():
            total_literacy += data["literacy"]

        avg_literacy = total_literacy / len(cities)

        print("Average Literacy =", avg_literacy)

        for city, data in cities.items():

            if data["literacy"] < avg_literacy:
                print(city, data)

    # 7. Population Density
    elif choice == 7:

        print("Population Density Report")

        for city, data in cities.items():

            density = data["population"] / data["area"]

            print(city, "Density =", round(density, 2))

    # 8. Highest Density City
    elif choice == 8:

        highest_density = -1
        density_city = ""

        for city, data in cities.items():

            density = data["population"] / data["area"]

            if density > highest_density:

                highest_density = density
                density_city = city

        print("Highest Density City =", density_city)
        print("Density =", round(highest_density, 2))

    # 9. Categorize Cities
    elif choice == 9:

        for city, data in cities.items():

            population = data["population"]

            if population < 5000000:
                category = "Small"

            elif population < 15000000:
                category = "Medium"

            else:
                category = "Large"

            print(city, "->", category)

    # 10. Development Priority List
    elif choice == 10:

        print("Development Priority Cities")

        for city, data in cities.items():

            if data["literacy"] < 90:
                print(city, data)

    # 11. High Literacy & Low Literacy Dictionaries
    elif choice == 11:

        high_literacy = {}
        low_literacy = {}

        for city, data in cities.items():

            if data["literacy"] >= 90:
                high_literacy[city] = data

            else:
                low_literacy[city] = data

        print("\nHigh Literacy Cities")
        print(high_literacy)

        print("\nLow Literacy Cities")
        print(low_literacy)

    # 12. National Summary Report
    elif choice == 12:

        total_population = 0
        total_area = 0

        for data in cities.values():

            total_population += data["population"]
            total_area += data["area"]

        print("\n===== NATIONAL SUMMARY REPORT =====")
        print("Total Cities =", len(cities))
        print("Total Population =", total_population)
        print("Total Area =", total_area)

    # 13. Rank Cities By Density (Without sort)
    elif choice == 13:

        temp = {}

        for city, data in cities.items():

            density = data["population"] / data["area"]

            temp[city] = density

        print("\nCity Ranking By Density")

        rank = 1

        while len(temp) > 0:

            max_city = ""
            max_density = -1

            for city, density in temp.items():

                if density > max_density:

                    max_density = density
                    max_city = city

            print(rank, ".", max_city,
                  "Density =", round(max_density, 2))

            del temp[max_city]

            rank += 1

    # 14. Exit
    elif choice == 14:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")