class Stack():
    def __init__(self, size: int):
        # List of items in stack
        self.items = [None for i in range(size)]
        
        # Points to item at top of stack
        self.top = -1

        # Sets maximum amount of items in stack
        self.size = size

    # Returns True if maximum amount of items in stack
    def is_full(self):
        if self.top == self.size - 1:
            return True
        return False

    # Returns True if no items in queue
    def is_empty(self):
        if self.top == -1:
            return True
        return False
    
    # Adds item to top of stack and increase top pointer by 1
    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full! Cannot push")
        
        else:
            self.top += 1
            self.items[self.top] = item

    # Returns top item on stack and decrease top pointer by 1
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty! Cannot pop")
    
        else:
            self.top -= 1
            return self.items[self.top + 1]
        
    # Return top item on stack without decreasing top pointer
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty! Cannot peek")
        
        else: return self.items[self.top]


    def __str__(self):
        if not self.is_empty():
            text = ""
            for i in range(self.top + 1):
                text += "|" + str(self.items[i]) + "|\n"
            return text
        else: return "STACK EMPTY!\n"