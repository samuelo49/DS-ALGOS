"""
in-order traversal, traverse the left subtree then the root then the right subtree

Left -> root -> right

this explores the tree in its natural ordering.

Same as traversing a tree and returning a sorted array.
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inOrderTraversal(node):
    if node:
        inOrderTraversal(node.left)
        print(node.val)
        inOrderTraversal(node.right)

    else:
        return []


def reverseInorderTraversal(node):
    if node:
        reverseInorderTraversal(node.right)
        print(node.val)
        reverseInorderTraversal(node.left)
    else:
        return []


leftLeft, leftRight = Node(2), Node(7)
rightLeft, rightRight = Node(12), Node(17)
left = Node(5, leftLeft, leftRight)
right = Node(15, rightLeft, rightRight)
root = Node(10, left, right)

# print(inOrderTraversal(root))
# print(reverseInorderTraversal(root))

