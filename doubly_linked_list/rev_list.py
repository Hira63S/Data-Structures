""" Reverse a Singly Linked List without recursion"""

# dummy head
# iterate through the List
# set each item as the new head
# keep the pointer at the next item and make it the head
class Node:
    def __init__(self, node):
        self.node = node
class Reverse:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def rev(list):
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current       # move the pointer
        self.head = prev         # make the previous item the head 
