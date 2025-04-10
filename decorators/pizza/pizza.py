from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def get_price(self):
        pass

    @property
    def description(self) -> str:
        return "pizza"
