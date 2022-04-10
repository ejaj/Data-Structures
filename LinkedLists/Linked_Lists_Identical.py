class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def areIdentical(self, listb):
        a = self.head
        b = listb.head
        while a is not None and b is not None:
            if a.data != b.data:
                return False
            a = a.next
            b = b.next
        return a == None and b == None


def areIdentical_recursive(a, b):
    if (a == None and b == None):
        return True
    if (a != None and b != None):
        return ((a.data == b.data) and areIdentical_recursive(a.next, b.next))
    return False


# Driver Code
llist1 = LinkedList()
llist2 = LinkedList()

# The constructed linked lists are :
# llist1: 3->2->1
# llist2: 3->2->1
llist1.push(1)
llist1.push(2)
llist1.push(3)
llist2.push(1)
llist2.push(2)
llist2.push(3)

if (llist1.areIdentical(llist2) == True):
    print("Identical ")
else:
    print("Not identical ")
