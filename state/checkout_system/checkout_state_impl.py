from checkout_system.checkout_state import CheckoutState
from checkout_system.checkout_context import CheckoutContext


class CartState(CheckoutState):
    def handle(self, context : CheckoutContext):
        return "Cart: Adding items to your cart."

class PaymentState(CheckoutState):
    def handle(self, context : CheckoutContext):
        return "Payment: Entering payment details."

class ConfirmationState(CheckoutState):
    def handle(self, context : CheckoutContext):
        return "Confirmation: Order confirmed and payment received."


