from strategy.discount_strategy import DiscountStrategy


# Concrete Strategy 1: Percentage Discount
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent

    def apply_discount(self, price: float, quantity: int) -> float:
        return price * quantity * ((100 - self.percent) / 100)


# Concrete Strategy 2: Fixed Discount
class FixedDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply_discount(self, price: float, quantity: int) -> float:
        total = (price * quantity) - self.amount
        return max(total, 0)


# Concrete Strategy 3: Buy-One-Get-One Free
class BOGODiscount(DiscountStrategy):
    def apply_discount(self, price: float, quantity: int) -> float:
        paid_items = (quantity // 2) + (quantity % 2)
        return paid_items * price
