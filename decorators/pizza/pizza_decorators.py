from pizza.pizza import Pizza
from abc import abstractmethod


class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    @abstractmethod
    def get_price(self):
        pass

    @property
    def description(self) -> str:
        return self.pizza.description
