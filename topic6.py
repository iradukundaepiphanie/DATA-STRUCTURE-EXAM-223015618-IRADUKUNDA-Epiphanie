class TreeNode:
    """A node in the hierarchical tree structure."""
    def __init__(self, name, data=None):
        self.name = name
        self.data = data  # Additional data for the node
        self.children = []

    def add_child(self, child_node):
        """Add a child node to the current node."""
        self.children.append(child_node)

    def remove_child(self, child_name):
        """Remove a child node by its name."""
        self.children = [child for child in self.children if child.name != child_name]

    def display(self, level=0):
        """Recursively display the tree structure."""
        indent = " " * (level * 4)
        print(f"{indent}{self.name}: {self.data}")
        for child in self.children:
            child.display(level + 1)

class EventHierarchy:
    """Tree structure to manage hierarchical data in the event management system."""
    def __init__(self):
        self.root = TreeNode("Event Management System")

    def find_node(self, current_node, name):
        """Recursively find a node by its name."""
        if current_node.name == name:
            return current_node

        for child in current_node.children:
            found_node = self.find_node(child, name)
            if found_node:
                return found_node

        return None

    def add_event(self, parent_name, event_name, data=None):
        """Add a new event under a specific parent node."""
        parent_node = self.find_node(self.root, parent_name)
        if parent_node:
            new_node = TreeNode(event_name, data)
            parent_node.add_child(new_node)
            print(f"Added '{event_name}' under '{parent_name}'.")
        else:
            print(f"Parent node '{parent_name}' not found.")

    def remove_event(self, event_name):
        """Remove an event by its name."""
        if self.root.name == event_name:
            print("Cannot remove the root node.")
            return

        def recursive_remove(node):
            for child in node.children:
                if child.name == event_name:
                    node.remove_child(event_name)
                    print(f"Removed event '{event_name}'.")
                    return True
                if recursive_remove(child):
                    return True
            return False

        if not recursive_remove(self.root):
            print(f"Event '{event_name}' not found.")

    def display_hierarchy(self):
        """Display the entire event hierarchy."""
        self.root.display()

# Example usage
def main():
    hierarchy = EventHierarchy()

    # Add some events
    hierarchy.add_event("Event Management System", "Weddings", "Wedding planning and management")
    hierarchy.add_event("Event Management System", "Conferences", "Conference planning and management")
    hierarchy.add_event("Weddings", "Venue Selection", "Choosing venues for weddings")
    hierarchy.add_event("Conferences", "Keynote Speakers", "Managing keynote speakers")
    hierarchy.add_event("Weddings", "Catering", "Arranging catering services")

    # Display the hierarchy
    print("Event Hierarchy:")
    hierarchy.display_hierarchy()

    # Remove an event
    hierarchy.remove_event("Venue Selection")

    # Display the hierarchy after removal
    print("\nEvent Hierarchy after removal:")
    hierarchy.display_hierarchy()

if __name__ == "__main__":
    main()
