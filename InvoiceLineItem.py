
def getprice():
    while True:
        try:
            price = float(input("Enter Price: "))
            return price
        except ValueError:
            print("Invalid Decimal Number. Please Try Again.")

def getquantity():
    while True:
        try:
            quantity = int(input("Enter Quantity: "))
            return quantity
        except ValueError:
            print("Invalid Integar. Please Try Again.")
def main():
    print("The Invoice Line Item Calculator")
    print()
    answer = "y"
    while answer.lower() == "y":
        price = getprice()
        quantity = getquantity()
        totals = price*quantity

        print()
        print("PRICE: ", f"{price: .2f}")
        print("QUANTITY: ", quantity)
        print("TOTAL: ", f"{totals: .2f}")
        answer = input("Enter Another Line Item? (y/n): ")
        print()
    print("Bye!!")

if __name__ == "__main__":
    main()