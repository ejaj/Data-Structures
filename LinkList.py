class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        """
        :param new_data:
        :return:
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to insert a new node to given node.
    def insertAfter(self, prev_node, new_data):
        """

        :param prev_node:
        :param new_data:
        :return:
        """
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Function to insert a new node at the end.
    def append(self, new_data):
        """

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

    # Given a reference to the head of a list and a key,
    # delete the first occurence of key in linked list
    def deleteNode(self, key):
        """
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

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


llist = LinkList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.insertAfter(llist.head.next, 6)
llist.append(4)
llist.deleteNode(1)
llist.printList()
