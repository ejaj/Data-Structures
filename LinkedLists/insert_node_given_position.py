class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)

    if head is None:
        head = SinglyLinkedListNode(data)
    else:
        current = head
        count = 1
        while current is not None and current < position:
            current = current.next
            count += 1
        node.next = current.next
        current.next = node
    return head
