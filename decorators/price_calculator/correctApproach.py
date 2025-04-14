# 🧱 The Core Structure
from abc import ABC, abstractmethod

class PriceCalculator(ABC):
    @abstractmethod
    def calculate(self, price: float) -> float:
        pass

    @property
    def description(self) -> str:
        return "Base Price"

# Base Price (no modifications)
class BasePrice(PriceCalculator):
    def calculate(self, price: float) -> float:
        if price < 0:
            raise ValueError("Price cannot be negative")
        return price

# 🧩 Decorators
# All decorators extend this shared base:
class DiscountDecorator(PriceCalculator):
    def __init__(self, wrapped: PriceCalculator):
        self.wrapped = wrapped

    @property
    def description(self) -> str:
        return self.wrapped.description

# ✅ Seasonal Discount
class SeasonalDiscount(DiscountDecorator):
    def __init__(self, wrapped: PriceCalculator, discount_percent: float = 10.0):
        super().__init__(wrapped)
        self.discount_percent = discount_percent

    def calculate(self, price: float) -> float:
        base_price = self.wrapped.calculate(price)
        return base_price * (1 - self.discount_percent / 100)

# ✅ Promo Code Discount
class PromoCodeDiscount(DiscountDecorator):
    def __init__(
        self,
        wrapped: PriceCalculator,
        discount_amount: float = 5.0,
        min_purchase: float = 0.0,
    ):
        super().__init__(wrapped)
        self.discount_amount = discount_amount
        self.min_purchase = min_purchase

    def calculate(self, price: float) -> float:
        base_price = self.wrapped.calculate(price)
        return (
            max(0, base_price - self.discount_amount)
            if base_price >= self.min_purchase
            else base_price
        )

# ✅ Loyalty Discount
class LoyaltyDiscount(DiscountDecorator):
    def __init__(self, wrapped: PriceCalculator, loyalty_level: int = 1):
        super().__init__(wrapped)
        self.discount_percent = loyalty_level * 2.5 + 2.5  # 5%, 7.5%, 10%

    def calculate(self, price: float) -> float:
        base_price = self.wrapped.calculate(price)
        return base_price * (1 - self.discount_percent / 100)

# ✅ Bulk Discount
class BulkDiscount(DiscountDecorator):
    def __init__(
        self,
        wrapped: PriceCalculator,
        quantity: int = 1,
        threshold: int = 10,
        discount_percent: float = 15.0,
    ):
        super().__init__(wrapped)
        self.quantity = quantity
        self.threshold = threshold
        self.discount_percent = discount_percent

    def calculate(self, price: float) -> float:
        base_price = self.wrapped.calculate(price)
        if self.quantity >= self.threshold:
            return base_price * (1 - self.discount_percent / 100)
        return base_price

# ✅ Tax Calculator
class TaxCalculator(DiscountDecorator):
    def __init__(self, wrapped: PriceCalculator, tax_rate: float = 8.25):
        super().__init__(wrapped)
        self.tax_rate = tax_rate

    def calculate(self, price: float) -> float:
        base_price = self.wrapped.calculate(price)
        return base_price * (1 + self.tax_rate / 100)
