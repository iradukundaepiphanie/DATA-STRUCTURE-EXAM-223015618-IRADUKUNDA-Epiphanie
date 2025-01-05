class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            return []
        if self.rear >= self.front:
            return self.queue[self.front : self.rear + 1]
        else:
            return self.queue[self.front :] + self.queue[: self.rear + 1]


import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        heapq.heappush(self.heap, item)

    def extract_min(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return heapq.heappop(self.heap)

    def peek_min(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def display(self):
        return sorted(self.heap)


# Example usage in an event management system
if __name__ == "__main__":
    # Managing event registration with a Circular Queue
    print("--- Circular Queue ---")
    event_queue = CircularQueue(5)
    event_queue.enqueue("Wedding 1")
    event_queue.enqueue("Conference 1")
    event_queue.enqueue("Wedding 2")
    print("Queue after enqueuing:", event_queue.display())

    print("Dequeued:", event_queue.dequeue())
    print("Queue after dequeuing:", event_queue.display())

    # Managing priority tasks with a MinHeap
    print("--- MinHeap ---")
    priority_heap = MinHeap()
    priority_heap.insert((2, "Setup Venue"))  # Priority 2
    priority_heap.insert((1, "Confirm Catering"))  # Priority 1
    priority_heap.insert((3, "Send Invitations"))  # Priority 3
    print("Heap after inserting tasks:", priority_heap.display())

    print("Extracted Min:", priority_heap.extract_min())
    print("Heap after extracting min:", priority_heap.display())