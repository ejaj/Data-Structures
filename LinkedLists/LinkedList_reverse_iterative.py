class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
     A Link List Class
    """

    def __init__(self):
        self.head = None

    def reverse(self):
        """
        Reverse link list
        :return:
        """
        prev = None
        current = self.head
        while current is not None:
            next = current.next

            current.next = prev
            prev = current

            current = next
        self.head = prev

    def push(self, new_data):
        """
        Inert a new node at the beginning.
        Time Complexity: O(1)
        :param new_data:
        :return:
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        """
        Print all value of linked list
        :return:
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next


def main():
    """
    Main function for drive code.
    :return:
    """
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)
    print("Given Linked List")
    llist.print_list()
    llist.reverse()
    print("\nReversed Linked List")
    llist.print_list()


if __name__ == '__main__':
    main()
