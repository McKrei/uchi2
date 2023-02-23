class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()


stack = Stack()

line = input()

operations = '+-*/'

for elem in line.split():
    if elem in operations:
        second_num = stack.pop()
        first_num = stack.pop()
        if elem == '+':
            stack.push(first_num + second_num)
        elif elem == '-':
            stack.push(first_num - second_num)
        elif elem == '*':
            stack.push(first_num * second_num)
        elif elem == '/':
            stack.push(first_num // second_num)
    else:
        stack.push(int(elem))
print(stack.pop())
