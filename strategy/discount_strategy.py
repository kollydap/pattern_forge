from abc import ABC, abstractmethod

# Strategy Interface
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: float, quantity: int) -> float:
        pass



