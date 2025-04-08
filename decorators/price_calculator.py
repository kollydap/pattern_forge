from abc import ABC, abstractmethod

class PriceCalculator(ABC):
    @abstractmethod
    def calculate(self, price: float) -> float:
        pass

class BasePrice(PriceCalculator):
    def calculate(self, price):
        return price

class DiscountDecorator(PriceCalculator):
    def __init__(self, wrapped: PriceCalculator):
        self.wrapped = wrapped

class SeasonalDiscount(DiscountDecorator):
    def calculate(self, price):
        return self.wrapped.calculate(price) * 0.9  # 10% off

class PromoCodeDiscount(DiscountDecorator):
    def calculate(self, price):
        return self.wrapped.calculate(price) - 5  # Flat $5 off

class LoyaltyDiscount(DiscountDecorator):
    def calculate(self, price):
        return self.wrapped.calculate(price) * 0.95  # 5% off

# Stack 'em!
price = LoyaltyDiscount(PromoCodeDiscount(SeasonalDiscount(BasePrice())))
print("Final Price: $", price.calculate(100))
