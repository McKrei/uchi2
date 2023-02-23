class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value


def print_linked_list(vertex):
    while vertex:
        print(vertex, end=" -> ")
        vertex = vertex.next
    print("None")


n3 = Node('third', None)
n2 = Node('second', n3)
n1 = Node('first', n2)
head = n1
print_linked_list(head)
