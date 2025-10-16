"""
When you have multiple ways to perform an operation, and you want to switch between them easily.
When you want to avoid using many conditional statements (if-else or switch) for selecting a behavior.
When related classes differ only in their behavior.

real-time eg..    A sorting class that can sort data using different algorithms (like quicksort, mergesort, bubblesort)
Payment strategies in e-commerce (Credit Card, PayPal, UPI).
Route planning in navigation apps (walk, public transport, car).
"""

from abc import ABC, abstractmethod

# 1. Strategy Interface (implicitly defined)
class BillingStrategy(ABC):
    @abstractmethod
    def calculate_bill(self, amount):
        raise NotImplementedError("Subclass must implement abstract method")

# 2. Concrete Strategies
class StandardDiscountStrategy(BillingStrategy):
    def calculate_bill(self, amount):
        # 10% discount
        return amount * 0.90

class PremiumDiscountStrategy(BillingStrategy):
    def calculate_bill(self, amount):
        # 20% discount
        return amount * 0.80

class NoDiscountStrategy(BillingStrategy):
    def calculate_bill(self, amount):
        return amount

# 3. Context
class ShoppingCart:
    def __init__(self, strategy: BillingStrategy):
        self._strategy = strategy
        self._items = []

    def set_strategy(self, strategy: BillingStrategy):
        self._strategy = strategy

    def add_item(self, price):
        self._items.append(price)

    def checkout(self):
        total_amount = sum(self._items)
        final_bill = self._strategy.calculate_bill(total_amount)
        print(f"Total items cost: ${total_amount:.2f}")
        print(f"Final bill after discount: ${final_bill:.2f}")

# Client Usage
cart = ShoppingCart(StandardDiscountStrategy()) # Starts with Standard Discount
cart.add_item(100)
cart.add_item(50)
cart.checkout()

print("-" * 20)

# Change strategy at runtime
cart.set_strategy(PremiumDiscountStrategy())
cart.add_item(20)
cart.checkout()