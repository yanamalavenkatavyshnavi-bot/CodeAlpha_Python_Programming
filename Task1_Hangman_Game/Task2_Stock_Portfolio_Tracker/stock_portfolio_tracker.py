stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

total = 0

name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if name in stocks:
    value = stocks[name] * quantity
    total += value

    print("\nStock:", name)
    print("Price:", stocks[name])
    print("Quantity:", quantity)
    print("Total Investment:", total)

    with open("portfolio.txt", "w") as file:
        file.write("Stock: " + name + "\n")
        file.write("Price: " + str(stocks[name]) + "\n")
        file.write("Quantity: " + str(quantity) + "\n")
        file.write("Total Investment: " + str(total))

    print("\nResult saved in portfolio.txt")

else:
    print("Stock not found!")
