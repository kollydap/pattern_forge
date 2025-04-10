import unittest
from price_calculator_decorator_impl import (
    SeasonalDiscount,
    PromoCodeDiscount,
    LoyaltyDiscount,
    BulkDiscount,
    TaxCalculator,
)
from prices import BasePrice


class TestPriceCalculator(unittest.TestCase):

    def setUp(self):
        """Set up common test fixtures"""
        self.base_price = BasePrice()

    def test_base_price(self):
        """Test the base price calculator."""
        self.assertEqual(self.base_price.calculate(100), 100)
        self.assertEqual(self.base_price.calculate(0), 0)

        with self.assertRaises(ValueError):
            self.base_price.calculate(-10)

    def test_description(self):
        """Test descriptions for all calculators."""
        self.assertEqual(self.base_price.description, "Base Price")

        seasonal = SeasonalDiscount(self.base_price)
        self.assertEqual(seasonal.description, "Base Price, Seasonal 10.0% Off")

        promo = PromoCodeDiscount(self.base_price, code="SUMMER")
        self.assertEqual(promo.description, "Base Price, $5.0 Off (Code: SUMMER)")

        loyalty = LoyaltyDiscount(self.base_price, loyalty_level=3)
        self.assertEqual(loyalty.description, "Base Price, Loyalty 10.0% Off (Level 3)")

        bulk = BulkDiscount(self.base_price, quantity=20)
        self.assertEqual(bulk.description, "Base Price, Bulk 15.0% Off (Applied)")

        tax = TaxCalculator(self.base_price)
        self.assertEqual(tax.description, "Base Price, 8.25% Tax")

    def test_seasonal_discount(self):
        """Test the seasonal discount calculator."""
        # Default 10% discount
        seasonal = SeasonalDiscount(self.base_price)
        self.assertEqual(seasonal.calculate(100), 90)

        # Custom discount percentage
        seasonal = SeasonalDiscount(self.base_price, discount_percent=20)
        self.assertEqual(seasonal.calculate(100), 80)

        # Test input validation
        with self.assertRaises(ValueError):
            SeasonalDiscount(self.base_price, discount_percent=101)

        with self.assertRaises(ValueError):
            SeasonalDiscount(self.base_price, discount_percent=-5)

    def test_promo_code_discount(self):
        """Test the promo code discount calculator."""
        # Default $5 off
        promo = PromoCodeDiscount(self.base_price)
        self.assertEqual(promo.calculate(100), 95)

        # Custom discount amount
        promo = PromoCodeDiscount(self.base_price, discount_amount=10)
        self.assertEqual(promo.calculate(100), 90)

        # Test minimum purchase requirement
        promo = PromoCodeDiscount(self.base_price, discount_amount=10, min_purchase=50)
        self.assertEqual(promo.calculate(100), 90)  # Meets minimum
        self.assertEqual(promo.calculate(40), 40)  # Doesn't meet minimum

        # Test that price never goes below zero
        promo = PromoCodeDiscount(self.base_price, discount_amount=150)
        self.assertEqual(promo.calculate(100), 0)

        # Test input validation
        with self.assertRaises(ValueError):
            PromoCodeDiscount(self.base_price, discount_amount=-10)

    def test_loyalty_discount(self):
        """Test the loyalty discount calculator."""
        # Level 1: 5% discount
        loyalty = LoyaltyDiscount(self.base_price, loyalty_level=1)
        self.assertEqual(loyalty.calculate(100), 95)

        # Level 2: 7.5% discount
        loyalty = LoyaltyDiscount(self.base_price, loyalty_level=2)
        self.assertAlmostEqual(loyalty.calculate(100), 92.5)

        # Level 3: 10% discount
        loyalty = LoyaltyDiscount(self.base_price, loyalty_level=3)
        self.assertEqual(loyalty.calculate(100), 90)

        # Test input validation
        with self.assertRaises(ValueError):
            LoyaltyDiscount(self.base_price, loyalty_level=0)

        with self.assertRaises(ValueError):
            LoyaltyDiscount(self.base_price, loyalty_level=4)

    def test_bulk_discount(self):
        """Test the bulk discount calculator."""
        # Default: 15% off for 10+ items
        bulk = BulkDiscount(self.base_price, quantity=5, threshold=10)
        self.assertEqual(bulk.calculate(100), 100)  # Below threshold

        bulk = BulkDiscount(self.base_price, quantity=10, threshold=10)
        self.assertEqual(bulk.calculate(100), 85)  # At threshold

        bulk = BulkDiscount(self.base_price, quantity=20, threshold=10)
        self.assertEqual(bulk.calculate(100), 85)  # Above threshold

        # Custom discount percentage
        bulk = BulkDiscount(self.base_price, quantity=10, discount_percent=25)
        self.assertEqual(bulk.calculate(100), 75)

        # Test input validation
        with self.assertRaises(ValueError):
            BulkDiscount(self.base_price, quantity=0)

        with self.assertRaises(ValueError):
            BulkDiscount(self.base_price, threshold=1)

        with self.assertRaises(ValueError):
            BulkDiscount(self.base_price, discount_percent=101)

    def test_tax_calculator(self):
        """Test the tax calculator."""
        # Default tax rate: 8.25%
        tax = TaxCalculator(self.base_price)
        self.assertAlmostEqual(tax.calculate(100), 108.25)

        # Custom tax rate
        tax = TaxCalculator(self.base_price, tax_rate=5)
        self.assertEqual(tax.calculate(100), 105)

        # Test input validation
        with self.assertRaises(ValueError):
            TaxCalculator(self.base_price, tax_rate=-5)

    def test_chained_discounts(self):
        """Test multiple discounts chained together."""
        # Base price: $100
        # Seasonal: 10% off -> $90
        # Promo: $5 off -> $85
        # Loyalty (L2): 7.5% off -> $78.625
        # Bulk (15 items): 15% off -> $66.83125
        # Tax: 8.25% -> $72.345

        base = BasePrice()
        seasonal = SeasonalDiscount(base)
        promo = PromoCodeDiscount(seasonal)
        loyalty = LoyaltyDiscount(promo, loyalty_level=2)
        bulk = BulkDiscount(loyalty, quantity=15)
        final = TaxCalculator(bulk)

        self.assertAlmostEqual(final.calculate(100), 72.34, places=2)

        # Test a different chain order to confirm it produces different results
        # Base -> Promo -> Seasonal -> Loyalty -> Bulk -> Tax
        base = BasePrice()
        promo = PromoCodeDiscount(base)
        seasonal = SeasonalDiscount(promo)
        loyalty = LoyaltyDiscount(seasonal, loyalty_level=2)
        bulk = BulkDiscount(loyalty, quantity=15)
        final = TaxCalculator(bulk)

        # Different order produces different result
        self.assertNotAlmostEqual(final.calculate(100), 72.34, places=2)

    def test_edge_cases(self):
        """Test edge cases for the price calculator."""
        # Test with zero price
        self.assertEqual(self.base_price.calculate(0), 0)

        seasonal = SeasonalDiscount(self.base_price)
        self.assertEqual(seasonal.calculate(0), 0)

        # Test with very small price
        promo = PromoCodeDiscount(self.base_price, discount_amount=1)
        self.assertEqual(promo.calculate(0.5), 0)

        # Test with very large price
        large_price = 1000000
        bulk = BulkDiscount(self.base_price, quantity=100)
        self.assertEqual(bulk.calculate(large_price), large_price * 0.85)


if __name__ == "__main__":
    unittest.main()
