"""
find max element in binary tree using recursion
"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_max(node: TreeNode):
    if not node:
        return float("-inf")
    return max(node.value, tree_max(node.left), tree_max(node.right))


print(tree_max(TreeNode(1, TreeNode(2), TreeNode(3))))