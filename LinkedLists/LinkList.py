class Node:
    def __init__(self, data):
        """
        :param data:
        """
        self.data = data
        self.next = None


class LinkList:
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

    def insert_after(self, prev_node, new_data):
        """
        Inert a new node after given node.
        :param prev_node:
        :param new_data:
        :return:
        """
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        """
        Inert a new node at the end.
        Time Complexity: O(1)
        :param new_data:
        :return:
        """
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        """
        Delete node, the first occurence of key in linked list.
        Time Complexity: O(n)
        :param key:
        :return:
        """
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        while cur_node is not None:
            if cur_node.data == key:
                break
            prev = cur_node
            cur_node = cur_node.next
        if cur_node == None:
            return
        prev.next = cur_node.next
        cur_node = None

    def print_list(self):
        """
        Print all node
        Time Complexity: O(n)
        :return:
        """
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


def main():
    """
    Main function to drive code
    :return:
    """
    llist = LinkList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.insert_after(llist.head.next, 6)
    llist.append(4)
    llist.delete_node(1)
    llist.print_list()


if __name__ == '__main__':
    main()
