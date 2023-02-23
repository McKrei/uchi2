
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


def insert_node(head, index, value):
    new_node = Node(value, None)
    if index == 0:
        new_node.next = head
        return new_node
    else:
        i = 0
        node = head
        while i < index - 1 and node.next is not None:
            node = node.next
            i += 1
        previous = node
        new_node.next = previous.next
        previous.next = new_node
        return head


n3 = Node('third', None)
n2 = Node('second', n3)
n1 = Node('first', n2)
head = n1
print_linked_list(head)
head = insert_node(head, 2, 'new_value')
print_linked_list(head)
