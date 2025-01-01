class Queue:
    def __init__(self, size):
        # Sets maximum amount of items in queue
        self.size = size

        # Points to next item to be dequeued
        self.front = 0

        # Points to last item in the queue
        self.rear = -1

        # List of items in queue
        self.queue = [None for i in range(size)]


    # Returns True if maximum amount of items in queue
    def is_full(self):
        if self.rear == self.front + self.size - 1:
            return True
        return False

    # Returns True if no items in queue
    def is_empty(self):
        if self.rear == self.front - 1:
            return True
        return False

    # Adds new item to end of queue
    def enqueue(self, item):
        if not self.is_full():
            self.rear += 1
            self.queue[self.rear % self.size] = item
        else:
            raise Exception("Queue is full! Cannot enqueue")

    # Returns item at start of list and increments front pointer
    def dequeue(self):
        if not self.is_empty():
            self.front += 1
            return self.queue[(self.front - 1) % self.size]
        else:
            raise Exception("Queue is empty! Cannot dequeue")
