class Stack():
    def __init__(self, size: int):
        self.items = [None for i in range(size)]
        
        self.front = -1
        self.size = size

    def is_full(self):
        if self.front == self.size - 1:
            return True
        return False

    def is_empty(self):
        if self.front == -1:
            return True
        return False
    
    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full! Cannot push")
        
        else:
            self.front += 1
            self.items[self.front] = item

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty! Cannot pop")
    
        else:
            self.front -= 1
            return self.items[self.front + 1]
        
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty! Cannot peek")
        
        else: return self.items[self.front]


    def __str__(self):
        if not self.is_empty():
            text = ""
            for i in range(self.front + 1):
                text += "|" + str(self.items[i]) + "|\n"
            return text
        else: return "STACK EMPTY!\n"