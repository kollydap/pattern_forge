import unittest

from .discount_strategy_impl import (
    PercentageDiscount,
    FixedDiscount,
    BOGODiscount,
)
from strategy.cart import Cart


class TestDiscountStrategies(unittest.TestCase):

    def test_percentage_discount_normal(self):
        discount = PercentageDiscount(20)
        self.assertAlmostEqual(discount.apply_discount(100, 2), 160)

    def test_percentage_discount_zero_percent(self):
        discount = PercentageDiscount(0)
        self.assertAlmostEqual(discount.apply_discount(50, 3), 150)

    def test_percentage_discount_full_percent(self):
        discount = PercentageDiscount(100)
        self.assertAlmostEqual(discount.apply_discount(200, 1), 0)

    def test_percentage_discount_negative(self):
        discount = PercentageDiscount(-10)
        # In a real-world app, you'd probably raise a ValueError
        self.assertAlmostEqual(discount.apply_discount(100, 1), 110)

    def test_percentage_discount_above_100(self):
        discount = PercentageDiscount(150)
        self.assertAlmostEqual(discount.apply_discount(100, 1), -50)

    def test_fixed_discount_normal(self):
        discount = FixedDiscount(50)
        self.assertAlmostEqual(discount.apply_discount(100, 3), 250)

    def test_fixed_discount_exact_total(self):
        discount = FixedDiscount(300)
        self.assertEqual(discount.apply_discount(100, 3), 0)

    def test_fixed_discount_exceeds_total(self):
        discount = FixedDiscount(400)
        self.assertEqual(discount.apply_discount(100, 3), 0)

    def test_fixed_discount_zero_amount(self):
        discount = FixedDiscount(0)
        self.assertEqual(discount.apply_discount(100, 2), 200)

    def test_fixed_discount_negative_amount(self):
        discount = FixedDiscount(-20)
        self.assertEqual(discount.apply_discount(50, 2), 120)

    def test_bogo_discount_even_quantity(self):
        discount = BOGODiscount()
        self.assertEqual(discount.apply_discount(100, 4), 200)

    def test_bogo_discount_odd_quantity(self):
        discount = BOGODiscount()
        self.assertEqual(discount.apply_discount(100, 5), 300)

    def test_bogo_discount_single_item(self):
        discount = BOGODiscount()
        self.assertEqual(discount.apply_discount(100, 1), 100)

    def test_bogo_discount_zero_quantity(self):
        discount = BOGODiscount()
        self.assertEqual(discount.apply_discount(100, 0), 0)

    def test_cart_with_strategy_switching(self):
        cart = Cart(100, 2, PercentageDiscount(10))
        self.assertEqual(cart.checkout(), 180)

        cart.strategy = FixedDiscount(30)
        self.assertEqual(cart.checkout(), 170)

        cart.strategy = BOGODiscount()
        self.assertEqual(cart.checkout(), 100)

    def test_zero_quantity_all_strategies(self):
        self.assertEqual(Cart(100, 0, PercentageDiscount(50)).checkout(), 0)
        self.assertEqual(Cart(100, 0, FixedDiscount(100)).checkout(), 0)
        self.assertEqual(Cart(100, 0, BOGODiscount()).checkout(), 0)


if __name__ == "__main__":
    unittest.main()
