class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack after pushing 1, 2, 3:", stack)  # Output: [1, 2, 3]
print("Popped item:", stack.pop())  # Output: 3
print("Stack after popping:", stack)  # Output: [1, 2]
print("Top item using peek:", stack.peek())  # Output: 2
print("Is stack empty?:", stack.is_empty())  # Output: False
print("Stack size:", stack.size())  # Output: 2
