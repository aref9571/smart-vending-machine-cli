from typing import Optional, List
from src.utils.change_calculator import calculate_change
from src.models.product import Product
from src.models.transaction import Transaction
from src.models.machine_state import MachineState
from src.storage.json_storage import JSONStorage


class VendingService:

    def __init__(self):
        self.storage = JSONStorage()
        self.machine: MachineState = self.storage.load_machine()
        self.current_balance: float = 0.0

    def insert_money(self, amount: float) -> float:

        if amount <= 0:
            raise ValueError("Amount must be positive")
        coin = int(round(amount*100))
        self.machine.cash_reserve[coin] = self.machine.cash_reserve.get(coin,0) + 1

        self.current_balance += amount
        self.storage.save_machine(self.machine)
        return self.current_balance

    def return_money(self) -> float:

        change = self.current_balance
        self.current_balance = 0.0
        return change

    def list_products(self) -> List[Product]:
        return self.machine.products

    def get_product(self, product_id: str) -> Optional[Product]:

        for product in self.machine.products:
            if product.id.startswith(product_id) :
                return product

        return None

    def buy_product(self, product_id: str) -> Transaction:

        product = self.get_product(product_id)

        if not product:
            raise ValueError("Product not found")

        if product.stock <= 0:
            raise ValueError("Product out of stock")

        if self.current_balance < product.price:
            raise ValueError("Insufficient balance")

        product.stock -= 1

        change = round(self.current_balance - product.price, 2)
        change_coins = calculate_change(change , self.machine.cash_reserve)
        for coin , qty in change_coins.items():
            self.machine.cash_reserve[coin]  -= qty
        transaction = Transaction(
            product_id=product.id,
            product_name=product.name,
            price=product.price,
            paid=self.current_balance,
            change=change
        )

        self.machine.transactions.append(transaction)

        self.current_balance = 0.0

        self.storage.save_machine(self.machine)

        return transaction

    def add_product(self, name: str, price: float, stock: int) -> Product:

        if price <= 0:
            raise ValueError("Price must be positive")

        if stock < 0:
            raise ValueError("Stock cannot be negative")

        product = Product(
            name=name,
            price=price,
            stock=stock
        )

        self.machine.products.append(product)

        self.storage.save_machine(self.machine)

        return product

    def restock_product(self, product_id: str, amount: int) -> bool:

        product = self.get_product(product_id)

        if not product:
            return False

        if amount <= 0:
            raise ValueError("Invalid restock amount")

        product.stock += amount

        self.storage.save_machine(self.machine)

        return True

    def remove_product(self, product_id: str) -> bool:

        initial_count = len(self.machine.products)

        self.machine.products = [
            p for p in self.machine.products if p.id != product_id
        ]

        removed = len(self.machine.products) < initial_count

        if removed:
            self.storage.save_machine(self.machine)

        return removed

    def total_sales(self) -> float:
        return sum(t.price for t in self.machine.transactions)

    def total_transactions(self) -> int:
        return len(self.machine.transactions)

    def most_popular_product(self) -> Optional[str]:

        counter = {}

        for t in self.machine.transactions:
            counter[t.product_name] = counter.get(t.product_name, 0) + 1

        if not counter:
            return None

        return max(counter, key=counter.get)
