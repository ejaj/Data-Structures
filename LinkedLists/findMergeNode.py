def findMergeNode(head1, head2):

    def getCount(head):
        n = 0
        while head.next is not None:
            head = head.next
            n += 1
        return n

    def getNode(d, head1, head2):
        for i in range(d):
            head1 = head1.next

        while head1 and head2:
            if head1 == head2:
                return head1.data
            else:
                head1 = head1.next
                head2 = head2.next

    c1 = getCount(head1)
    c2 = getCount(head2)
    if c1>c2:
        return getNode(c1 - c2, head1, head2)
    else:
        return getNode(c2-c1, head2, head1)


