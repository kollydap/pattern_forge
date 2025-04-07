from checkout_system.checkout_state import CheckoutState
from checkout_system.checkout_context import CheckoutContext


class CartState(CheckoutState):
    def handle(self, context):
        """Handle the cart state: verify if user can proceed to payment"""
        print("Processing cart...")

        if not context.has_sufficient_funds():
            print("Insufficient funds. Cannot proceed to payment.")
            return False

        print("Cart validated. Proceeding to payment.")
        context.set_state(PaymentState())
        return True


class PaymentState(CheckoutState):
    def handle(self, context):
        """Handle the payment state: process the payment"""
        print("Processing payment...")

        # Simulate payment processing
        context.user_info["balance"] -= context.get_total_cost()

        print(f"Payment successful. Remaining balance: {context.user_info['balance']}")

        # Move to confirmation state
        context.set_state(ConfirmationState())
        return True


class ConfirmationState(CheckoutState):
    def handle(self, context):
        """Handle the confirmation state: complete the order"""
        print("Order confirmed!")
        print(
            f"Purchased {context.product_info['quantity']} items at ${context.product_info['price']} each"
        )
        print(f"Total cost: ${context.get_total_cost()}")
        print(f"Your remaining balance: ${context.user_info['balance']}")
        return True
