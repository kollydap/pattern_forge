from strategy.discount_strategy import DiscountStrategy

# Context
class Cart:
    def __init__(
        self, price_per_item: float, quantity: int, strategy: DiscountStrategy
    ):
        self.price_per_item = price_per_item
        self.quantity = quantity
        self.strategy = strategy

    def checkout(self) -> float:
        return self.strategy.apply_discount(self.price_per_item, self.quantity)
