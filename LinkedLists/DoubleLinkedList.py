import gc


class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoublyLinkedList:
    """
    A Double Linked List Class
    """

    def __init__(self):
        self.head = None

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

    def insert_after(self, prev_node, new_data):
        """

        :param prev_node:
        :param new_data:
        :return:
        """
        if prev_node is None:
            print("the given previous node cannot be NULL")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    def append(self, new_data):
        """
        Inert a new node at the end.
        Time Complexity: O(n)
        :param new_data:
        :return:
        """
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        return

    def delete_node(self, dele):

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

    def print_list(self, node):
        """

        :param node:
        :return:
        """
        print("\nTraversal in forward direction")
        while node:
            print(" % d" % (node.data))
            last = node
            node = node.next

        print("\nTraversal in reverse direction")
        while last:
            print(" % d" % (last.data))
            last = last.prev


def main():
    llist = DoublyLinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)
    llist.insert_after(llist.head.next, 8)

    print("Created DLL is: ", llist.print_list(llist.head))


if __name__ == '__main__':
    main()
