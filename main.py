from strategy.cart import Cart
from strategy.discount_strategy_impl import PercentageDiscount, FixedDiscount, BOGODiscount
from decorators.price_calculator.prices import BasePrice
from decorators.price_calculator.price_calculator_decorator_impl import SeasonalDiscount, PromoCodeDiscount, LoyaltyDiscount, BulkDiscount,TaxCalculator

# Example usage
def strategy():
    price = 100
    quantity = 3

    cart1 = Cart(price, quantity, PercentageDiscount(10))
    cart2 = Cart(price, quantity, FixedDiscount(50))
    cart3 = Cart(price, quantity, BOGODiscount())

    print("Percentage Discount:", cart1.checkout())
    print("Fixed Discount:", cart2.checkout())
    print("BOGO Discount:", cart3.checkout())


def decorator():
    # Start with base price of $100
    base_price = BasePrice()
    print(f"Base Price: ${base_price.calculate(100):.2f}")
    
    # Add seasonal discount (10% off)I
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