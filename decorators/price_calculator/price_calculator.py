from abc import ABC, abstractmethod

class PriceCalculator(ABC):
    """Abstract base class for price calculation operations."""
    
    @abstractmethod
    def calculate(self, price: float) -> float:
        """Calculate the price after applying any modifications."""
        pass
    
    @property
    def description(self) -> str:
        """Return a description of the price calculation."""
        return "Base Price"


