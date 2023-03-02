class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.queue_size = 0

    def pop(self):
        if not self.queue_size:
            print('error')
        else:
            print(self.head.value)
            self.head = self.head.next
            self.queue_size -= 1

    def push(self, x):
        if not self.head:
            self.head = Node(x, None)
            self.tail = self.head
        else:
            new = Node(x, None)
            self.tail.next = new
            self.tail = new
        self.queue_size += 1

    def size(self):
        print(self.queue_size)


n = int(input())
queue = Queue()
for i in range(n):
    commands = input().split()
    if commands[0] == 'size':
        queue.size()
    elif commands[0] == 'pop':
        queue.pop()
    elif commands[0] == 'push':
        queue.push(int(commands[1]))
