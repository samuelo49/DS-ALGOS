"""buildRightChildOnlyTree
Q. Construct a right child only tree from a given array.

Q. Construct a right child only tree from a given array.
Input: [1, 2, 3]
Output:
          1
            \
              2
                \
                 3
"""


class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printBinaryTree(arr):
    def helper(array, root):
        if len(array) == 1:
            return
        if root is None:
            root = BinaryTreeNode(array[0])

        root.right = helper(array[1:len(array)], root)
        return root

    return helper(arr, None)


# print(printBinaryTree([1, 2, 3]))


def printB(root: BinaryTreeNode):
    if root:
        print(root.val)
        print(root.right)

print(printB(printBinaryTree([1, 2, 3])))
