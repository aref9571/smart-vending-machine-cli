import sys
from src.services.vending_service import VendingService


def print_menu():
    print("\nSMART VENDING MACHINE")
    print("---------------------")
    print("1. View Products")
    print("2. Insert Money")
    print("3. Buy Product")
    print("4. Return Money")
    print("5. Admin: Add Product")
    print("6. Admin: Restock")
    print("7. Exit")


def show_products(service: VendingService):
    products = service.list_products()

    if not products:
        print("No products available.")
        return

    print("\nAvailable Products\n")

    for p in products:
        print(f"{p.id[:8]} | {p.name} | ${p.price:.2f} | stock:{p.stock}")


def insert_money(service: VendingService):
    try:
        amount = float(input("Insert amount: "))
        balance = service.insert_money(amount)
        print(f"Current balance: ${balance:.2f}")
    except ValueError as e:
        print(e)


def buy_product(service: VendingService):
    pid = input("Enter product id (first 8 chars): ").strip()

    try:
        t = service.buy_product(pid)

        print("\nPurchase successful")
        print(f"Product: {t.product_name}")
        print(f"Paid: ${t.paid:.2f}")
        print(f"Change: ${t.change:.2f}")

    except ValueError as e:
        print(e)


def return_money(service: VendingService):
    change = service.return_money()
    print(f"Returned: ${change:.2f}")


def add_product(service: VendingService):
    name = input("Name: ").strip()

    try:
        price = float(input("Price: "))
        stock = int(input("Stock: "))

        p = service.add_product(name, price, stock)

        print(f"Added {p.name} ({p.id[:8]})")

    except ValueError as e:
        print(e)


def restock(service: VendingService):
    pid = input("Product id: ")
    amount = int(input("Amount: "))

    if service.restock_product(pid, amount):
        print("Restocked.")
    else:
        print("Product not found.")


def main():

    service = VendingService()

    while True:

        print_menu()

        choice = input("Select option: ").strip()

        if choice == "1":
            show_products(service)

        elif choice == "2":
            insert_money(service)

        elif choice == "3":
            buy_product(service)

        elif choice == "4":
            return_money(service)

        elif choice == "5":
            add_product(service)

        elif choice == "6":
            restock(service)

        elif choice == "7":
            print("Goodbye.")
            sys.exit()

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
