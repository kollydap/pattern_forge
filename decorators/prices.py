from decorators.price_calculator import PriceCalculator

# concrete 
class BasePrice(PriceCalculator):
    """Basic price with no modifications."""
    
    def calculate(self, price: float) -> float:
        """Return the original price without modifications."""
        if price < 0:
            raise ValueError("Price cannot be negative")
        return price
    
    @property
    def description(self) -> str:
        return "Base Price"
