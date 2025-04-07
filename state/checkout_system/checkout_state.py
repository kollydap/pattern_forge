from abc import ABC, abstractmethod


class CheckoutState(ABC):
    @abstractmethod
    def handle(self):
        pass
        