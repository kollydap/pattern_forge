from abc import ABC, abstractmethod
from typing import Optional

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

class DiscountDecorator(PriceCalculator):
    """Base decorator class for applying discounts."""
    
    def __init__(self, wrapped: PriceCalculator):
        """Initialize with the component to wrap."""
        self.wrapped = wrapped
    
    @property
    def description(self) -> str:
        """Return description of the wrapped component."""
        return self.wrapped.description

class SeasonalDiscount(DiscountDecorator):
    """Applies a seasonal percentage discount."""
    
    def __init__(self, wrapped: PriceCalculator, discount_percent: float = 10.0):
        """
        Initialize with the component to wrap and discount percentage.
        
        Args:
            wrapped: The price calculator to wrap
            discount_percent: Percentage discount (default 10%)
        """
        super().__init__(wrapped)
        if not 0 <= discount_percent <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        self.discount_percent = discount_percent
    
    def calculate(self, price: float) -> float:
        """Apply seasonal discount after wrapped calculation."""
        base_price = self.wrapped.calculate(price)
        discount_factor = 1 - (self.discount_percent / 100)
        return base_price * discount_factor
    
    @property
    def description(self) -> str:
        return f"{self.wrapped.description}, Seasonal {self.discount_percent}% Off"

class PromoCodeDiscount(DiscountDecorator):
    """Applies a flat amount discount."""
    
    def __init__(self, wrapped: PriceCalculator, discount_amount: float = 5.0, 
                 min_purchase: float = 0.0, code: Optional[str] = None):
        """
        Initialize with component to wrap and discount amount.
        
        Args:
            wrapped: The price calculator to wrap
            discount_amount: Flat amount to discount (default $5)
            min_purchase: Minimum purchase required for promo (default $0)
            code: Optional promo code identifier
        """
        super().__init__(wrapped)
        if discount_amount < 0:
            raise ValueError("Discount amount cannot be negative")
        self.discount_amount = discount_amount
        self.min_purchase = min_purchase
        self.code = code
    
    def calculate(self, price: float) -> float:
        """Apply flat discount after wrapped calculation."""
        base_price = self.wrapped.calculate(price)
        
        # Only apply discount if price meets minimum purchase requirement
        if base_price >= self.min_purchase:
            # Ensure price doesn't go below zero
            return max(0, base_price - self.discount_amount)
        return base_price
    
    @property
    def description(self) -> str:
        code_str = f" (Code: {self.code})" if self.code else ""
        min_str = f" (Min. ${self.min_purchase})" if self.min_purchase > 0 else ""
        return f"{self.wrapped.description}, ${self.discount_amount} Off{code_str}{min_str}"

class LoyaltyDiscount(DiscountDecorator):
    """Applies a percentage discount based on loyalty status."""
    
    def __init__(self, wrapped: PriceCalculator, loyalty_level: int = 1):
        """
        Initialize with component to wrap and loyalty level.
        
        Args:
            wrapped: The price calculator to wrap
            loyalty_level: Customer loyalty level (1-3, higher = more discount)
        """
        super().__init__(wrapped)
        if not 1 <= loyalty_level <= 3:
            raise ValueError("Loyalty level must be between 1 and 3")
        self.loyalty_level = loyalty_level
        
        # Discount increases with loyalty level: 5%, 7.5%, 10%
        self.discount_percent = self.loyalty_level * 2.5 + 2.5
    
    def calculate(self, price: float) -> float:
        """Apply loyalty discount after wrapped calculation."""
        base_price = self.wrapped.calculate(price)
        discount_factor = 1 - (self.discount_percent / 100)
        return base_price * discount_factor
    
    @property
    def description(self) -> str:
        return f"{self.wrapped.description}, Loyalty {self.discount_percent}% Off (Level {self.loyalty_level})"

class BulkDiscount(DiscountDecorator):
    """Applies a discount based on quantity purchased."""
    
    def __init__(self, wrapped: PriceCalculator, quantity: int = 1, 
                 threshold: int = 10, discount_percent: float = 15.0):
        """
        Initialize with component to wrap and bulk purchase details.
        
        Args:
            wrapped: The price calculator to wrap
            quantity: Number of items being purchased
            threshold: Minimum quantity to qualify for discount
            discount_percent: Discount percentage when threshold is met
        """
        super().__init__(wrapped)
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        if threshold < 2:
            raise ValueError("Threshold must be at least 2")
        if not 0 <= discount_percent <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")
            
        self.quantity = quantity
        self.threshold = threshold
        self.discount_percent = discount_percent
    
    def calculate(self, price: float) -> float:
        """Apply bulk discount if quantity threshold is met."""
        # First calculate through wrapped components
        base_price = self.wrapped.calculate(price)
        
        # Apply bulk discount if quantity meets threshold
        if self.quantity >= self.threshold:
            discount_factor = 1 - (self.discount_percent / 100)
            return base_price * discount_factor
        return base_price
    
    @property
    def description(self) -> str:
        status = "Applied" if self.quantity >= self.threshold else "Not Applied"
        return f"{self.wrapped.description}, Bulk {self.discount_percent}% Off ({status})"

class TaxCalculator(DiscountDecorator):
    """Applies tax after all discounts."""
    
    def __init__(self, wrapped: PriceCalculator, tax_rate: float = 8.25):
        """
        Initialize with component to wrap and tax rate.
        
        Args:
            wrapped: The price calculator to wrap
            tax_rate: Tax rate percentage (default 8.25%)
        """
        super().__init__(wrapped)
        if tax_rate < 0:
            raise ValueError("Tax rate cannot be negative")
        self.tax_rate = tax_rate
    
    def calculate(self, price: float) -> float:
        """Apply tax after all other calculations."""
        base_price = self.wrapped.calculate(price)
        tax_factor = 1 + (self.tax_rate / 100)
        return base_price * tax_factor
    
    @property
    def description(self) -> str:
        return f"{self.wrapped.description}, {self.tax_rate}% Tax"

# Example usage:
if __name__ == "__main__":
    # Start with base price of $100
    base_price = BasePrice()
    print(f"Base Price: ${base_price.calculate(100):.2f}")
    
    # Add seasonal discount (10% off)
    with_seasonal = SeasonalDiscount(base_price)
    print(f"With Seasonal Discount: ${with_seasonal.calculate(100):.2f}")
    
    # Add promo code ($5 off)
    with_promo = PromoCodeDiscount(with_seasonal, code="SAVE5")
    print(f"With Promo Code: ${with_promo.calculate(100):.2f}")
    
    # Add loyalty discount (Level 2 = 7.5% off)
    with_loyalty = LoyaltyDiscount(with_promo, loyalty_level=2)
    print(f"With Loyalty: ${with_loyalty.calculate(100):.2f}")
    
    # Add bulk discount for 15 items (15% off)
    with_bulk = BulkDiscount(with_loyalty, quantity=15, threshold=10)
    print(f"With Bulk Discount: ${with_bulk.calculate(100):.2f}")
    
    # Finally, add tax
    final_price = TaxCalculator(with_bulk)
    print(f"Final Price with Tax: ${final_price.calculate(100):.2f}")
    print(f"Price Description: {final_price.description}")