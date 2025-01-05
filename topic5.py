class Node:
    """A node in a singly linked list."""
    def __init__(self, order_id, event_type):
        self.order_id = order_id
        self.event_type = event_type
        self.next = None

class SinglyLinkedList:
    """A singly linked list to dynamically track orders."""
    def __init__(self):
        self.head = None

    def add_order(self, order_id, event_type):
        """Add a new order to the end of the linked list."""
        new_node = Node(order_id, event_type)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Order added: {{'order_id': {order_id}, 'event_type': '{event_type}'}}")

    def remove_order(self, order_id):
        """Remove an order by its ID."""
        if not self.head:
            print("No orders to remove.")
            return

        # If the head is the order to remove
        if self.head.order_id == order_id:
            removed_order = self.head
            self.head = self.head.next
            print(f"Order removed: {{'order_id': {removed_order.order_id}, 'event_type': '{removed_order.event_type}'}}")
            return

        # Search for the order to remove
        current = self.head
        while current.next and current.next.order_id != order_id:
            current = current.next

        if current.next:  # Order found
            removed_order = current.next
            current.next = current.next.next
            print(f"Order removed: {{'order_id': {removed_order.order_id}, 'event_type': '{removed_order.event_type}'}}")
        else:
            print(f"Order with ID {order_id} not found.")

    def list_orders(self):
        """List all orders in the linked list."""
        if not self.head:
            print("No orders in the system.")
            return

        print("Current orders:")
        current = self.head
        while current:
            print({"order_id": current.order_id, "event_type": current.event_type})
            current = current.next

# Example usage
def main():
    order_manager = SinglyLinkedList()

    # Add some orders
    order_manager.add_order(101, "Wedding")
    order_manager.add_order(102, "Conference")
    order_manager.add_order(103, "Wedding")
    order_manager.add_order(104, "Conference")

    # List all orders
    order_manager.list_orders()

    # Remove an order
    order_manager.remove_order(102)

    # List all orders again
    order_manager.list_orders()

    # Attempt to remove a non-existent order
    order_manager.remove_order(999)

if __name__ == "__main__":
    main()