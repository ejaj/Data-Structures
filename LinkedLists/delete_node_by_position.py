class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
def deleteNode(head, position):
    if position == 0:
        head = head.next
    else:
        current = head
        count = 1
        while current is not None and count < position:
            current = current.next
            count += 1

        current.next = current.next.next

    return head
