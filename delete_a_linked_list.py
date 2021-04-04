class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_node):
        new_node = Node(new_node)
        new_node.next = self.head
        self.head = new_node

    def deleteList(self):
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev


# Use push() to construct below
# list 1-> 12-> 1-> 4-> 1
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)

    print("Deleting linked list")
    llist.deleteList()

    print("Linked list deleted")
