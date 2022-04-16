class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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

    def get_count(self):
        """
        Get total node count
        :return:
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


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
    print("Count of nodes is :", llist.get_count())


if __name__ == '__main__':
    main()
