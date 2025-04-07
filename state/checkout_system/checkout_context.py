from checkout_system.checkout_state_impl import CartState
from checkout_system.checkout_state import CheckoutState


# checkout_system/checkout_context.py
class CheckoutContext:
    def __init__(self, user_balance=0, product_price=0, product_quantity=0):
        from checkout_system.checkout_state_impl import CartState
        
        # Store user and product data
        self.user_info = {
            "balance": user_balance,
        }
        
        self.product_info = {
            "price": product_price, 
            "quantity": product_quantity
        }
        
        # Initialize with default state
        self.state = CartState()
    
    def set_state(self, state):
        """Change the current state of the checkout process"""
        self.state = state
    
    def handle(self):
        """Execute the current state's behavior"""
        self.state.handle(self)
    
    def get_total_cost(self):
        """Calculate the total cost of items in cart"""
        return self.product_info["price"] * self.product_info["quantity"]
    
    def has_sufficient_funds(self):
        """Check if user has enough balance to complete purchase"""
        return self.user_info["balance"] >= self.get_total_cost()

