class Node:
    """
    A Node Class
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
     A Double Linked List Class
    """

    def __init__(self):
        self.head = None

    def reverse(self):
        """
        Reverse double linked list
        :return:
        """
        temp = None
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev

    def push(self, new_data):
        """
        Inert a new node at the beginning.
        Time Complexity: O(1)
        :param new_data:
        :return:
        """
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def print_list(self, node):
        while node is not None:
            print(node.data)
            node = node.next


def main():
    """
    Main Function for drive code
    :return:
    """
    dll = DoublyLinkedList()
    dll.push(2)
    dll.push(4)
    dll.push(8)
    dll.push(10)

    print("\nOriginal Linked List")
    dll.print_list(dll.head)

    # Reverse doubly linked list
    dll.reverse()

    print("\n Reversed Linked List")
    dll.print_list(dll.head)


if __name__ == '__main__':
    main()
