from strategy.cart import Cart
from strategy.discount_strategy_impl import PercentageDiscount, FixedDiscount, BOGODiscount

# Example usage
if __name__ == "__main__":
    price = 100
    quantity = 3

    cart1 = Cart(price, quantity, PercentageDiscount(10))
    cart2 = Cart(price, quantity, FixedDiscount(50))
    cart3 = Cart(price, quantity, BOGODiscount())

    print("Percentage Discount:", cart1.checkout())
    print("Fixed Discount:", cart2.checkout())
    print("BOGO Discount:", cart3.checkout())
