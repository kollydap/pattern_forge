# checkout_system/checkout_state.py
from abc import ABC, abstractmethod

class CheckoutState(ABC):
    @abstractmethod
    def handle(self, context):
        """Handle the checkout process for the current state"""
        pass
