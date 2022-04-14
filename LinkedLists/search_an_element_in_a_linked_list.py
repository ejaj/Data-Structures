class Node:
    def __init__(self, data):
        """
        :param data:
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A Link List Class
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
        self.head = new_node

    def search(self, x):
        """
        Search node
        Time Complexity: O(n)
        :param x:
        :return:
        """
        current = self.head
        while current:
            if current.data == x:
                return True
            current = current.next
        return False


def main():
    """
    Main function to drive code
    :return:
    """
    llist = LinkedList()
    llist.push(10)
    llist.push(30)
    llist.push(11)
    llist.push(21)
    llist.push(14)

    if llist.search(21):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
