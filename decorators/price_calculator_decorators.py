from decorators.price_calculator import PriceCalculator


class DiscountDecorator(PriceCalculator):
    """Base decorator class for applying discounts."""

    def __init__(self, wrapped: PriceCalculator):
        """Initialize with the component to wrap."""
        self.wrapped = wrapped

    @property
    def description(self) -> str:
        """Return description of the wrapped component."""
        return self.wrapped.description
