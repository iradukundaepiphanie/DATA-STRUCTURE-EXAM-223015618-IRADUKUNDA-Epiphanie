class Event:
    def __init__(self, event_id, name, date, type, capacity, location):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.type = type  # 'wedding' or 'conference'
        self.capacity = capacity
        self.location = location
        self.attendees = []
        self.status = "Scheduled"  # Scheduled, In Progress, Completed, Cancelled

    def add_attendee(self, attendee_name):
        if len(self.attendees) < self.capacity:
            self.attendees.append(attendee_name)
            return True
        return False

    def remove_attendee(self, attendee_name):
        if attendee_name in self.attendees:
            self.attendees.remove(attendee_name)
            return True
        return False

    def update_status(self, new_status):
        valid_statuses = ["Scheduled", "In Progress", "Completed", "Cancelled"]
        if new_status in valid_statuses:
            self.status = new_status
            return True
        return False

class Node:
    def __init__(self, event):
        self.event = event
        self.next = None
        self.prev = None

class EventManagementSystem:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_event(self, event):
        new_node = Node(event)
        self.size += 1

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        # Add to end of list
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def remove_event(self, event_id):
        current = self.head

        while current:
            if current.event.event_id == event_id:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.size -= 1
                return True

            current = current.next
        return False

    def find_event(self, event_id):
        current = self.head
        while current:
            if current.event.event_id == event_id:
                return current.event
            current = current.next
        return None

    def get_events_by_type(self, event_type):
        events = []
        current = self.head
        while current:
            if current.event.type.lower() == event_type.lower():
                events.append(current.event)
            current = current.next
        return events

    def get_events_by_date(self, date):
        events = []
        current = self.head
        while current:
            if current.event.date == date:
                events.append(current.event)
            current = current.next
        return events

    def display_all_events(self):
        events = []
        current = self.head
        while current:
            events.append({
                'id': current.event.event_id,
                'name': current.event.name,
                'date': current.event.date,
                'type': current.event.type,
                'capacity': current.event.capacity,
                'location': current.event.location,
                'attendees': len(current.event.attendees),
                'status': current.event.status
            })
            current = current.next
        return events

# Example usage:
def main():
    # Initialize the event management system
    ems = EventManagementSystem()

    # Create sample events
    wedding1 = Event(1, "Smith Wedding", "2025-06-15", "wedding", 100, "Grand Hotel")
    conference1 = Event(2, "Tech Conference 2025", "2025-07-20", "conference", 500, "Convention Center")
    wedding2 = Event(3, "Johnson Wedding", "2025-08-01", "wedding", 150, "Beach Resort")

    # Add events to the system
    ems.add_event(wedding1)
    ems.add_event(conference1)
    ems.add_event(wedding2)

    # Add attendees to events
    wedding1.add_attendee("John Doe")
    wedding1.add_attendee("Jane Smith")
    conference1.add_attendee("Alice Johnson")
    conference1.add_attendee("Bob Wilson")

    # Update event status
    wedding1.update_status("In Progress")
    
    # Display all events
    print("All Events:")
    for event in ems.display_all_events():
        print(f"Event: {event['name']} ({event['type']})")
        print(f"Date: {event['date']}")
        print(f"Location: {event['location']}")
        print(f"Status: {event['status']}")
        print(f"Attendees: {event['attendees']}/{event['capacity']}")
        print("---")

    # Find specific events
    print("\nWeddings:")
    weddings = ems.get_events_by_type("wedding")
    for wedding in weddings:
        print(f"- {wedding.name} on {wedding.date}")

if __name__ == "__main__":
    main()
