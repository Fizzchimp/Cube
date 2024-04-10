from tkinter import END


class Queue:
    def __init__(self, size):
        self.size = size
        self.front = 0
        self.rear = -1
        
        self.queue = [None for i in range(size)]


    def isFull(self):
        if self.rear == self.front + self.size - 1:
            return True
        return False
        
    def isEmpty(self):
        if self.rear == self.front - 1:
            return True
        return False


    def enqueue(self, item):
        if not self.isFull():
            self.rear += 1
            self.queue[self.rear] = item
        else: print("Queue is full! Cannot enqueue")
     
    def dequeue(self):
        if not self.isEmpty():
            self.front += 1
            return self.queue[self.front - 1]
        else: print("Queue is empty! Cannot dequeue")
    

    def display(self):
        for i in range(self.front, self.rear):
            print(self.queue[i], end = ", ")


q = Queue(9)

for i in range(20):
    q.enqueue(i)
    
print(q.dequeue())
q.display()