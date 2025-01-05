from collections import deque

class OrderDeque:
    def __init__(self, max_orders):
        """Initialize the deque with a fixed size."""
        self.orders = deque(maxlen=max_orders)
        self.max_orders = max_orders

    def add_order(self, order_id, event_type):
        """Add a new order to the deque. Removes the oldest order if the deque is full."""
        order = {"order_id": order_id, "event_type": event_type}
        self.orders.append(order)
        print(f"Order added: {order}")

    def remove_oldest_order(self):
        """Remove the oldest order from the deque."""
        if self.orders:
            removed_order = self.orders.popleft()
            print(f"Removed oldest order: {removed_order}")
            return removed_order
        else:
            print("No orders to remove.")
            return None

    def remove_latest_order(self):
        """Remove the latest order from the deque."""
        if self.orders:
            removed_order = self.orders.pop()
            print(f"Removed latest order: {removed_order}")
            return removed_order
        else:
            print("No orders to remove.")
            return None

    def list_orders(self):
        """List all current orders in the deque."""
        if self.orders:
            print("Current orders:")
            for order in self.orders:
                print(order)
        else:
            print("No orders in the system.")

# Example usage
def main():
    max_orders = 5
    order_manager = OrderDeque(max_orders)

    # Add some orders
    order_manager.add_order(101, "Wedding")
    order_manager.add_order(102, "Conference")
    order_manager.add_order(103, "Wedding")
    order_manager.add_order(104, "Conference")
    order_manager.add_order(105, "Wedding")

    # List all orders
    order_manager.list_orders()

    # Add a new order, causing the oldest to be removed
    order_manager.add_order(106, "Conference")

    # List all orders again
    order_manager.list_orders()

    # Remove the oldest and the latest order
    order_manager.remove_oldest_order()
    order_manager.remove_latest_order()

    # List all orders again
    order_manager.list_orders()

if __name__ == "__main__":
    main()