"""
Q. Given a binary search tree and a target element's value, insert the target in the appropriate position.

Examples:
• Given a binary search tree:
              6
            /   \
           3     8
          / \
         2   4

• For target: 7 // returns:
              6
            /   \
           3     8
          / \    /
         2   4  7
        /     \
       1       5

• For target: 1 // returns:
              6
            /   \
           3     8
          / \
         2   4
        /
       1
"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def arrayifyTree(root: TreeNode):
    if root is None:
        return []
    queue = []
    array = []
    queue.append(root)
    while len(queue) != 0:
        node = queue.pop(0)
        array.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return array


def insert_bst(root: TreeNode, target: int) -> TreeNode:
    if not root:
        return TreeNode(target)
    curr = root
    while curr:
        if target < curr.value:
            if curr.left:
                curr = curr.left
            else:
                curr.left = TreeNode(target)
                return root
        else:
            if curr.right:
                curr = curr.right
            else:
                curr.right = TreeNode(target)
                return root


# Test Cases
tree = TreeNode(6, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8))
print(arrayifyTree(insert_bst(tree, 7)))  # [6, 3, 8, 2, 4, 7]
print(arrayifyTree(insert_bst(tree, 5)))  # [6, 3, 8, 2, 4, 7, 5]
print(arrayifyTree(insert_bst(tree, 1)))  # [6, 3, 8, 2, 4, 7, 1, 5]
print(arrayifyTree(insert_bst(None, 1)))  # [1]

# Given tree:
#              6
#            /   \
#           3     8
#          / \    /
#         2   4  7
#        /     \
#       1       5


def insert_bst(bst: Node, val: int) -> Node:
    if bst is None:
        return Node(val)
    if bst.val < val:
        bst.right = insert_bst(bst.right, val)
    elif bst.val > val:
        bst.left = insert_bst(bst.left, val)
    return bst