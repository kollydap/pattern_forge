from pizza.pizza_decorators import PizzaDecorator


class PeperoniToppings(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_price(self):
        return super().get_price() + 90

    @property
    def description(self) -> str:
        return f"{super().description}, with Peperoni Toppings"


class ExtraCheeseToppings(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_price(self):
        return super().get_price() + 72

    @property
    def description(self) -> str:
        return f"{super().description}, with ExtraCheese Toppings"


class BaconToppings(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_price(self):
        return super().get_price() + 30

    @property
    def description(self) -> str:
        return f"{super().description}, with Bacon Toppings"
