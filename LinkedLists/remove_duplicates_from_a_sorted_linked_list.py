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

    def deleteNode(self, key):
        current = self.head
        if current is not None:
            if current.data == key:
                self.head = current.next
                current = None
                return
        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.next
        if current == None:
            return

        prev.next = current.next

        current = None

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self):
        current = self.head
        if current is None:
            return
        while current.next is not None:
            if current.data == current.next.data:
                new = current.next.next
                current.next = None
                current.next = new
            else:
                current = current.next
        return self.head


llist = LinkedList()

llist.push(20)
llist.push(13)
llist.push(13)
llist.push(11)
llist.push(11)
llist.push(11)
print("Created Linked List: ")
llist.printList()
print()
print("Linked List after removing", "duplicate elements:")
llist.removeDuplicates()
llist.printList()