class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

n4 = Node('apple', None)
n3 = Node('banana', n4)
n2 = Node('orange', n3)
n1 = Node('grapes', n2)

s = input()
node = n1
index = 1

while node is not None:
    if node.value == s:
        print(index)
        break
    node = node.next
    index += 1
else:
    print(-1)
