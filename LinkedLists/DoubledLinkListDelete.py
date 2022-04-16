import gc


class Node:
    """
    Node Class
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    A class for doubly linked list
    """

    def __init__(self):
        self.head = None

    def delete_node(self, dele):
        """
        Deleted match
        :param dele:
        :return:
        """
        # head and dele both are None
        if self.head is None or dele is None:
            return
        # If node to be deleted is head node
        if self.head == dele:
            self.head = dele.next

        # Change next only if node to be deleted is NOT the last node
        if dele.next is not None:
            dele.next.prev = dele.prev

        # Change prev only if node to be deleted is NOT the first node
        if dele.prev is not None:
            dele.prev.next = dele.next
        gc.collect()

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
        """
        Print all linked list value
        :param node:
        :return:
        """
        while node is not None:
            print(node.data)
            node = node.next


def main():
    """
    Main function for drive code
    :return:
    """
    dll = DoublyLinkedList()
    dll.push(2)
    dll.push(4)
    dll.push(8)
    dll.push(10)

    print("\n Original Linked List")
    dll.print_list(dll.head)
    dll.delete_node(dll.head)
    dll.delete_node(dll.head.next)
    dll.delete_node(dll.head.next)
    print("\n Modified Linked List")
    dll.print_list(dll.head)


if __name__ == '__main__':
    main()
