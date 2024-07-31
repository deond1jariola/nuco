class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create nodes
main = Node(1)
main.next = Node(2)

# Assign the 'main' node to 'current'
current = main

# Traverse the linked list
while current is not None:
    print(current.value)
    current = current.next
