from abc import ABC, abstractmethod

# Observer Interface
class OrderObserver(ABC):
    @abstractmethod
    def update(self, order_id, status):
        pass

# Concrete Observers
class EmailService(OrderObserver):
    def update(self, order_id, status):
        print(f"[Email] Order {order_id} is now {status}")

class InventoryService(OrderObserver):
    def update(self, order_id, status):
        print(f"[Inventory] Adjusting stock for order {order_id}, status: {status}")

class DashboardService(OrderObserver):
    def update(self, order_id, status):
        print(f"[Dashboard] Order {order_id} updated to {status}")

# Subject
class OrderManager:
    def __init__(self):
        self._observers = []
        self._order_status = {}

    def attach(self, observer: OrderObserver):
        self._observers.append(observer)

    def detach(self, observer: OrderObserver):
        self._observers.remove(observer)

    def notify(self, order_id, status):
        for observer in self._observers:
            observer.update(order_id, status)

    def update_order(self, order_id, status):
        self._order_status[order_id] = status
        print(f"Order {order_id} status changed to {status}")
        self.notify(order_id, status)

# Usage
order_manager = OrderManager()

# Register observers
order_manager.attach(EmailService())
order_manager.attach(InventoryService())
order_manager.attach(DashboardService())

# Update an order
order_manager.update_order("ORD-001", "Shipped")
