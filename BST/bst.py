class Node:
    """
    A Class Tree
    """

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def in_order(node):
    """
    In order traverse
    :param node:
    :return:
    """
    if node is not None:
        in_order(node.left)
        print(str(node.key))
        in_order(node.right)


def insert(node, key):
    """
    Insert a value to the BST.
    Time Complexity: O(log n)
    :param node:
    :param key:
    :return:
    """
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def lookup(node, key):
    """
    Search the value fro BST.
    Time Complexity: O(log n)
    :param node:
    :param key:
    :return:
    """
    if node is None or node.key == key:
        return node
    if key < node.key:
        return lookup(node.left, key)
    else:
        return lookup(node.right, key)


def min_value_node(node):
    """
    Min value for the node
    :param node:
    :return:
    """
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete_node(node, key):
    """
    Delete node from the BST.
    Time Complexity: O(log n)
    :param node:
    :param key:
    :return:
    """
    if node is None:
        return node
    if key < node.key:
        node.left = delete_node(node.left, key)
    elif key > node.key:
        node.right = delete_node(node.right, key)
    else:
        # If the node is with only one child or no child
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        # If the node has two children,
        temp = min_value_node(node.right)
        node.key = temp.key
        node.right = delete_node(node.right, temp.key)
        return node


def main():
    """
    Main function for drive code
    :return:
    """
    root = None
    root = insert(root, 8)
    root = insert(root, 3)
    root = insert(root, 1)
    root = insert(root, 6)
    root = insert(root, 7)
    root = insert(root, 10)
    root = insert(root, 14)
    root = insert(root, 4)

    print("Inorder traversal: ", end=' ')
    in_order(root)

    print("\nDelete 10")
    root = delete_node(root, 10)
    print("Inorder traversal: ", end=' ')
    in_order(root)


if __name__ == '__main__':
    main()
