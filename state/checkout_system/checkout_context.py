from checkout_system.checkout_state_impl import CartState
from checkout_system.checkout_state import CheckoutState


class CheckoutContext():
    def __init__(self):
        # default state
        self.state = CartState()
        
    def setState(self,state : CheckoutState):
        self.state = state
    
    def handle(self, )
    
    