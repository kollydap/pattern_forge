class InventorySystem:
    def check_inventory(self, product_id):
        return f"Product {product_id} is in stock"
    
    def update_inventory(self, product_id):
        return f"Product {product_id} quantity reduced"

class PaymentProcessor:
    def process_payment(self, amount):
        return f"Payment of ${amount} processed successfully"

class ShippingSystem:
    def create_shipment(self, address):
        return f"Shipment created for {address}"
    
    def generate_label(self, order_id):
        return f"Shipping label generated for order {order_id}"

class OrderFacade:
    def __init__(self, inventory, payment, shipping):
        self.inventory = inventory
        self.payment = payment
        self.shipping = shipping
    
    def place_order(self, product_id, price, address, order_id):
        results = []
        results.append(self.inventory.check_inventory(product_id))
        results.append(self.payment.process_payment(price))
        results.append(self.inventory.update_inventory(product_id))
        results.append(self.shipping.create_shipment(address))
        results.append(self.shipping.generate_label(order_id))
        return "\n".join(results)