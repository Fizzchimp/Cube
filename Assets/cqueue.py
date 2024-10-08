class Queue:
    def __init__(self, size):
        self.size = size
        self.front = 0
        self.rear = -1

        self.queue = [None for i in range(size)]


    def is_full(self):
        if self.rear == self.front + self.size - 1:
            return True
        return False

    def is_empty(self):
        if self.rear == self.front - 1:
            return True
        return False

    def enqueue(self, item):
        if not self.is_full():
            self.rear += 1
            self.queue[self.rear % self.size] = item
        else:
            raise Exception("Queue is full! Cannot enqueue")

    def dequeue(self):
        if not self.is_empty():
            self.front += 1
            return self.queue[(self.front - 1) % self.size]
        else:
            raise Exception("Queue is empty! Cannot dequeue")


    def display(self):
        front, rear = self.front % self.size, self.rear % self.size
        print("==============")
        if not self.is_empty():
            print("[", end = "")
            for i in range(self.front, self.rear):
                print(self.queue[i % self.size], end = ", ")
            print(str(self.queue[rear]) + "]")
            print("Front:", self.queue[front])
            print("Rear:", self.queue[rear])
        else:
            print("Queue is empty!")
        print("Items:", self.rear - self.front + 1)
        print("Spaces:", self.size - (self.rear - self.front + 1), "\n==============")


    def findInstances(self, item):
        count = 0
        for i in range(self.front, self.rear + 1):
            if self.queue[i % self.size] == item:
                count += 1
        return count
