class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def reverse(head):
    while head.next is not None:
        head.next, head.prev, head = head.prev, head.next, head.next

    head.next, head.prev = head.prev, None

    return head


