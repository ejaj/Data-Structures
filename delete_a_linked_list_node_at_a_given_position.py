class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, position):

        if self.head == None:
            return

        current = self.head

        if position == 0:
            self.head = current.next
            current = None
            return

        for i in range(position -1):
            current = current.next
            if current is None:
                break

        if current is None:
            return
        if current.next is None:
            return

        next = current.next.next
        current.next = None
        current.next = next

    def printList(self):
        current = self.head
        while current:
            print(" %d " % current.data)
            current = current.next


llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)

print("Created Linked List: ")
llist.printList()
llist.deleteNode(4)
print("\nLinked List after Deletion at position 4: ")
llist.printList()
