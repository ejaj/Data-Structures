class Node:
    """
    A Node Class
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A Linked List Class
    """

    def __init__(self):
        self.head = None

    def push(self, new_data):
        """
        insert node
        :param new_data:
        :return:
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def get_count_rec(self, node):
        """
        :param node:
        :return:
        """
        if not node:
            return 0
        else:
            return 1 + self.get_count_rec(node.next)

    def get_count(self):
        """
        :return:
        """
        return self.get_count_rec(self.head)


def main():
    """
    Main function for drive code
    :return:
    """
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    print('Count of nodes is :', llist.get_count())


if __name__ == '__main__':
    main()
