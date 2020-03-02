""" find the middle of the linked list """

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self, head, list):
        self.head = node

    def add(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def midpoint(root):
        slow = root.head # starting point of the list
        fast = root.head

        while fast.next:
            if fast.next.next is None:
                return slow.value
            fast = fast.next.next
            slow = slow.next
        return slow.value
