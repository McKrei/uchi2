class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return f'{self.items}'

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
